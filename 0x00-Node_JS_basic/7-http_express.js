// small HTTP server using Express module
// same as 6-http_server.js with the addition of the following:
// '/' => 'Hello Holberton School!'
// '/students/ => 'This is the list of our students' + list of students

const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  await countStudents(process.argv[2])
    .then((data) => {
      res.write('This is the list of our students\n');
      res.write(`Number of students: ${data.CS.num + data.SWE.num}\n`);
      res.write(`Number of students in CS: ${data.CS.num}. List: ${data.CS.list}\n`);
      res.write(`Number of students in SWE: ${data.SWE.num}. List: ${data.SWE.list}`);
      res.end();
    })
    .catch((err) => {
      res.write('This is the list of our students\n');
      res.end(err.message);
    });
}).listen(port);

module.exports = app;
