// same as 3-read_file_async.js with the addition of the following:
// '/' => 'Hello Holberton School!'`
// '/students' => 'This is the list of students' followed by the
// same content as the file 3-read_file_async.js
// Name of the database passed as arugment to file

const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  if (req.url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  }
  if (req.url === '/students') {
    res.write('This is the list of students\n');
    const checkArg = '';
    try {
      if (process.argv[2] === checkArg) {
        throw new Error();
      }
      const students = await countStudents(process.argv[2]);
      res.write(students);
    } catch (error) {
      res.write('Cannot load the Database');
    }
  }
  res.end();
}).listen(1245);

module.exports = app;
