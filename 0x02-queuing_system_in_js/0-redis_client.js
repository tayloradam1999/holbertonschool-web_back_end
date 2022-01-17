// Using Babel, connects to Redis server

const redis = require('redis');
const client = redis.createClient();

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

client.on('error', (err) => {
	console.log('Redis client not connected to then server: ' + err);
});
