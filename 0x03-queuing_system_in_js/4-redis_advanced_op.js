import { createClient } from "redis";

import redis from "redis";

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server:', err));

client.on('connect', () => console.log('Redis client connected to the server'));

function hashSet(hashKey, key, value) {
  client.hset(hashKey, key, value, redis.print);
};

function hashGetAll(hashKey) {
  client.hgetall(hashKey, (value, err) => {
    if (value) {
      console.log(value);
    } else {
      console.error(err);
    }
  });
};

hashSet('HolbertonSchools', 'Portland', '50');
hashSet('HolbertonSchools', 'Seattle', '80');
hashSet('HolbertonSchools', 'New York', '20');
hashSet('HolbertonSchools', 'Bogota', '20');
hashSet('HolbertonSchools', 'Cali', '40');
hashSet('HolbertonSchools', 'Paris', '2');

hashGetAll('HolbertonSchools');
