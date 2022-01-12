// use beforeEach hook and afterEach hook to test 5-payment.js
const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');
const sinon = require('sinon');
const { expect } = require('chai');


describe('Test suite', function () {
	let spy;

	beforeEach(function () {
		spy = sinon.spy(console, 'log');
	});

	afterEach(function () {
		spy.restore();
	});

	it('Uses a spy to validate response from console.log for 120', function () {
		sendPaymentRequestToApi(100, 20);
		expect(spy.calledWith('The total is: 120')).to.be.true;
		expect(spy.calledOnce).to.be.true;
	});

	it('Uses a spy to validate response from console.log for 20', function () {
		sendPaymentRequestToApi(10, 10);
		expect(spy.calledWith('The total is: 20')).to.be.true;
		expect(spy.calledOnce).to.be.true;
	});
})