import { createClient } from "redis";
import { promisify } from "util";

import redis from "redis";

const client = createClient();
const getAysnc = promisify(client.get).bind(client);

client.on('error', err => console.log('Redis client not connected to the server:', err));

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
};

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAysnc(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
