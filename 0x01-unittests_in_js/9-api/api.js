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
// :id must only be a number (validation in route definition)
app.get('/cart/:id(\\d+)/', (req, res) => {
	res.send(`Payment methods for cart ${req.params.id}`);
});
// export app
module.exports = app;
