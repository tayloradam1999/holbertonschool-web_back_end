const getPaymmentTokenFromApi = require('./6-payment_token');
const chai = require('chai');


// utilizes 'done' for async testing
describe('Test suite', function () {
	it('Tests that getPaymentTokenFromApi returns a new Promise', function (done) {
		getPaymmentTokenFromApi(true).then(function (result) {
			chai.expect(result).to.be.an('object');
			done();
		});
	});
})