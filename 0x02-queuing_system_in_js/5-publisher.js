// Manages publisher for a queue

const redis = require('redis');
const client = redis.createClient();


(async() => {
	client.on('error', (err) => {
		console.log('Redis client not connected to the server: ' + err);
	}).on('ready', () => {
		console.log(`Redis client connected to the server`);
	});
	await client.connect();
})();

const publishMessage = (message, time) => {
	// after setTimeout, publish message to channel
	setTimeout(() => {
		console.log(`About to send ${message}`);
		client.publish('holberton school channel', message);
	}, time);
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
