var calculateNumber = require('./0-calcul')
var chai = require('chai');
var assert = require('assert');


describe ("test suite", function() {
	it("Tests if first number is rounded", function () {
		assert.equal(calculateNumber(4.5,5), 10);
	});
	it("Tests if second number is rounded", function () {
		assert.equal(calculateNumber(4,5.5), 10);
	});
	it("Tests if both numbers are rounded", function () {
		assert.equal(calculateNumber(4.5,5.5), 11);
	});
});