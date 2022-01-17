// Manages subscribers for a queue

const redis = require('redis');
const client = redis.createClient();

// on load, connect to redis
(async() => {
	client.on('error', (err) => {
		console.log('Redis client not connected to the server: ' + err);
	}).on('ready', () => {
		console.log(`Redis client connected to the server`);
	});
	await client.connect();
})();

// subscribe to channel 'holberton school channel'
client.subscribe('holberton school channel');

// on message, log message to console
client.on('message', (channel, message) => {
	console.log(`${message}`);
	if (message === 'KILL_SERVER') {
		client.unsubscribe(channel);
		process.exit(0);
	}
});
