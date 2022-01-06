// small HTTP server using http module
// assigned to <app> and exported
// listens on port 1245
// displays text for any endpoint

const app = require('http');

const host = 'localhost';
const port = 1245;

const requestListener = function write(req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Helllo Holberton School!\n');
};

const server = app.createServer(requestListener);
server.listen(port, host, () => {
  console.log('Server running');
});
