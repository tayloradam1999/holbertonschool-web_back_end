// Uses redis client to store a hash value
const redis = require('redis');
const client = redis.createClient();


// handles loading the redis client
(async() => {
	client.on('error', (err) => {
		console.log('Redis client not connected to the server: ' + err);
	}).on('ready', () => {
		console.log(`Redis client connected to the server`);
	});
	await client.connect();
})();

// Set up values for Hash
const hashKey = 'HolbertonSchools';
const hashValues = {
	'Portland': '100',
	'Seattle': '80',
	'New York': '20',
	'Bogota': '20',
	'Cali': '40',
	'Paris': '2'
};
// Iterates through hashValues and assigns key and value to redis
for (let key in hashValues) {
	const hSet = client.hSet(hashKey, hashValues, hashValues[key], redis.print, (err, reply) => {
		if (err) {
			console.log(err);
		}
		return reply;
	}).then(res => {
		console.log(`Reply: ${res + 1}`);
	});
}
// Use hGetAll to display all values in hash
const hGetAll = client.hGetAll(hashKey, (err, reply) => {
	if (err) {
		console.log(err);
	}
	return reply;
}
).then(res => {
	console.log(res);
});
