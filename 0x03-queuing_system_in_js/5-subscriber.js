import { createClient } from "redis";

const client = createClient();
// const subscriber = client.duplicate();

client.on('error', err => console.log('Redis client not connected to the server:', err));

client.on('connect', () => console.log('Redis client connected to the server'));

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    console.log(message);
    client.unsubscribe('holberton school channel');
    client.quit();
  } else {
    console.log(message);
  }
});
