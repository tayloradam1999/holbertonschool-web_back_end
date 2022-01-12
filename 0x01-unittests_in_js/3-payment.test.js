// by using sinon.spy, compares sendPaymentRequestToApi to Utils.calculateNumber
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');
const sinon = require('sinon');
const { expect } = require('chai');


describe('sendPaymentRequestToApi', function () {
	it('Validates the usage of the Utils function in sendPaymentRequestToApi', function () {
		const spy = sinon.spy(Utils, 'calculateNumber');
		sendPaymentRequestToApi(100, 20);
		expect(spy.calledWith('SUM', 100, 20)).to.be.true;
		expect(spy.calledOnce).to.be.true;
		spy.restore();
	});
})
