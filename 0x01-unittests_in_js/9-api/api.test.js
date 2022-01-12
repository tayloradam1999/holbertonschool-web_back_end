// Unittest file for api.js
const { expect } = require('chai');
const mocha = require('mocha');
const request = require('request');


// Test suite for index page
describe('Test suite for index page for api.js', () => {
	// Correct status code for index page
	it ('Checks for correct HTTP status code', (done) => {
		request('http://localhost:7865', (error, response, body) => {
			expect(response.statusCode).to.equal(200);
			done();
		});
	});
	// Correct result for index page 'Welcome to the payment system'
	it ('Checks for correct result for index page', (done) => {
		request('http://localhost:7865', (error, response, body) => {
			expect(body).to.equal('Welcome to the payment system');
			done();
		});
	});
});


// Test suite for cart page
describe('Test suite for cart page for api.js', () => {
	// Correct status code when :id is a number
	it ('Checks for correct HTTP status code when :id is a number', (done) => {
		request('http://localhost:7865/cart/1', (error, response, body) => {
			expect(response.statusCode).to.equal(200);
			done();
		});
	});
	// Correct status code when :id is not a number
	it ('Checks for correct HTTP status code when :id is not a number', (done) => {
		request('http://localhost:7865/cart/a', (error, response, body) => {
			expect(response.statusCode).to.equal(400);
			done();
		});
	});
})
