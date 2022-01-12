// by using sinon.spy and sinon.stub, compares sendPaymentRequestToApi to Utils.calculateNumber
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');
const sinon = require('sinon');
const { expect } = require('chai');


describe('sendPaymentRequestToApi', function () {
	it('Stubs calculateNumber to always return 10 and verifies', function () {
		const stub = sinon.stub(Utils, 'calculateNumber').callsFake(() => 10);
		const spy = sinon.spy(console, 'log');
		sendPaymentRequestToApi(100, 20);
		expect(stub.calledWith('SUM', 100, 20)).to.be.true;
		expect(spy.calledWith('The total is: 10')).to.be.true;
		stub.restore();
		spy.restore();
	});
})
