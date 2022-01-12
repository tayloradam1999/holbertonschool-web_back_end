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
// export app
module.exports = app;
