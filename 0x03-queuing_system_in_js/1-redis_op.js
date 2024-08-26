import { createClient } from "redis";

import redis from "redis";

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server', err));

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
};

function displaySchoolValue(schoolName) {
  client.get(schoolName, (value, err) => {
    if (value) {
      console.log(value);
    } else {
      console.error(err);
    };
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
