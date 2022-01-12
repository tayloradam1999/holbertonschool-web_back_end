const Utils = require('./utils');

// function to be tested by 4-payment.test.js
function sendPaymentRequestToApi(totalAmount, totalShipping) {
	const result = Utils.calculateNumber('SUM', totalAmount, totalShipping);
	console.log(`The total is: ${result}`);
}

module.exports = sendPaymentRequestToApi;