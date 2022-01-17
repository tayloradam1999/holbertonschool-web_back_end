// Using Babel, connects to Redis server

const redis = require('redis');
const client = redis.createClient();

(async () => {
	client.on('error', (err) => {
		console.log('Redis client not connected to the server: ' + err);
	}).on('ready', () => {
		console.log(`Redis client connected to the server`);
	});

	await client.connect();
})();
