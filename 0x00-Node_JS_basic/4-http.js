// small HTTP server using http module
// assigned to <app> and exported
// listens on port 1245
// displays text for any endpoint

import { createServer } from 'http';

const host = 'localhost'
const port = 1245

const requestListener = function (req, res) {
	res.writeHead(200, { 'Content-Type': 'text/plain' });
	res.end('Helllo Holberton School!\n');
}

const server = createServer(requestListener);
server.listen(port, host, () => {
	console.log('Server running at http://' + host + ':' + port + '/');
})