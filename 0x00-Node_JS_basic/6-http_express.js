// small HTTP server using Express module
// same as 4-http_server.js but only responds to '/'

const express = require('express');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(port, () => {
  console.log('Server is running');
});

module.exports = app;
