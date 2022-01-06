// same as 3-read_file_async.js with the addition of the following:
// '/' => 'Hello Holberton School!'`
// '/students' => 'This is the list of students' followed by the
// same content as the file 3-read_file_async.js
// Name of the database passed as arugment to file

const countStudents = require('./3-read_file_async');
const http = require('http');


const app = http.createServer((req, res) => {
	res.writeHead(200, { 'Content-Type': 'text/html' });
	if (req.url === '/') {
		res.end('Hello Holberton School!');
	}
	else if (req.url === '/students') {
		res.end('This is the list of students' <br> + countStudents('./database.csv'));
	}
	else {
		throw new Error('Not a valid URL');
	}
  }).listen(1245);
  