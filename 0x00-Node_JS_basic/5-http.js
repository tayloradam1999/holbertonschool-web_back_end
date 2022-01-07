// same as 3-read_file_async.js with the addition of the following:
// '/' => 'Hello Holberton School!'`
// '/students' => 'This is the list of students' followed by the
// same content as the file 3-read_file_async.js
// Name of the database passed as arugment to file

const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  if (req.method === 'GET') {
    if (req.url === '/') {
      res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
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
    }
  }
}).listen(1245);

module.exports = app;
