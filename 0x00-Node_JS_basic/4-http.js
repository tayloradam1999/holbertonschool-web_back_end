// small HTTP server using http module
// assigned to <app> and exported
// listens on port 1245
// displays text for any endpoint

const http = require('http');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end('Hello Holberton School!');
}).listen(1245);

module.exports = app;
