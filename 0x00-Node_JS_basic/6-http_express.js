// small HTTP server using Express module
// same as 4-http_server.js but only responds to '/'

const express = require('express');
const app = express();


app.get('/', (req, res) => {
	res.send('Hello Holberton School!');
});

module.exports = app;