import { createClient } from "redis";

const client = createClient();
const subscriber = client.duplicate();

client.on('error', err => console.log('Redis client not connected to the server:', err));

client.on('connect', () => console.log('Redis client connected to the server'));

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    console.log(message);
    subscriber.unsubscribe('holberton school channel');
    subscriber.quit();
  } else {
    console.log(message);
  }
});
