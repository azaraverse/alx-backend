import redis, { createClient } from 'redis';
import { promisify } from 'util';
import { createQueue } from 'kue';

const express = require('express');

const client = createClient();
const getAsync = promisify(client.get).bind(client);
const queue = createQueue();
const app = express();

const port = 1245;

function reserveSeat(number) {
  client.set('available_seats', number, redis.print);
}

async function getCurrentAvailableSeats() {
  try {
    const value = await getAsync('available_seats');
    return value;
  } catch (err) {
    console.error(err);
  }
}

const initialAvailableSeats = 50;
let reservationEnabled = true;

reserveSeat(initialAvailableSeats);

app.get('/available_seats', async (request, response) => {
  const seatsAvailable = await getCurrentAvailableSeats();
  response.json({ numberOfAvailableSeats: seatsAvailable });
});

app.get('/reserve_seat', async (request, response) => {
  const seatsAvailable = await getCurrentAvailableSeats();

  if (seatsAvailable <= 0) {
    reservationEnabled = false;
  }

  if (!reservationEnabled) {
    return response.json({ status: 'Reservation are blocked' });
  }

  if (seatsAvailable > 0 && reservationEnabled) {
    const job = queue.create('reserve_seat');
    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    });
    job.on('failed', (err) => {
      console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });

    job.save((err) => {
      if (!err) {
        return response.json({ status: 'Reservation in process' });
      }
      return response.json({ status: 'Reservation failed' });
    });
  }
});

app.get('/process', (request, response) => {
  queue.process('reserve_seat', async (job, done) => {
    try {
      const seatsAvailable = await getCurrentAvailableSeats();

      if (seatsAvailable === 0) {
        reservationEnabled = false;
      }

      if (seatsAvailable > 0) {
        reserveSeat(seatsAvailable - 1);
      }

      done();
    } catch (err) {
      done(err);
    }
  });
  return response.json({ status: 'Queue processing' });
});

app.listen(port);
