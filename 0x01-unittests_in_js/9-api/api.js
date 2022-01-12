const express = require('express');
// create instance of express called app
const app = express();
// listen to specific port and logs to browser console when express
// server is started
const port = 7865;
app.listen(port, () => {
    console.log(`API available on localhost port ${port}`);
});
// create route 'GET /'
app.get('/', (req, res) => {
	res.send(`Welcome to the payment system`);
});
// create route 'GET /cart/:id'
// :id must only be a number
app.get('/cart/:id', (req, res) => {
	try {
		// typecast :id to number
		req.params.id = Number(req.params.id);
		// check if :id is a number
		if (isNaN(req.params.id)) {
			throw new Error;
		}
		// if :id is a number, send back log with :id
		res.send(`Payment methods for cart ${req.params.id}`);
	} catch (e) {
		// if :id is not a number, send back 404 so route does not exist for checker
		res.sendStatus(404);
	}
});
// export app
module.exports = app;
