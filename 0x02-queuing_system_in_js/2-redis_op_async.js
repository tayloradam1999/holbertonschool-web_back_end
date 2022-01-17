// Using Babel, connects to Redis server

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


// sets a a new <schoolName, value> pair
function setNewSchool(schoolName, value) {
	const setKey = client.set(schoolName, value, (err, reply) => {
		if (err) {
			console.log(err);
		}
		return reply;
	});
	setKey.then(res => {
		console.log(`Result: ${res.toString()}`);
	});
}

// async function to display the value of a <schoolName, value> pair
async function displaySchoolValue(schoolName) {
	const getKey = client.get(schoolName, (err, reply) => {
		if (err) {
			console.log(err);
		}
		return reply;
	});
	await getKey.then(res => {
		console.log(res);
	});
}

// assign schoolName and value to function
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
