var calculateNumber = require('./0-calcul')
var chai = require('chai');
var assert = require('assert');


describe ("test suite for first number", function() {
	it("Tests if first number is rounded", function () {
		assert.equal(calculateNumber(4.5,5), 10);
	});
});

describe ("test suite for second number", function() {
	it("Tests if second number is rounded", function () {
		assert.equal(calculateNumber(5,4.5), 10);
	});
});

describe ("test suite for both numbers", function() {
	it("Tests if both numbers are rounded", function () {
		assert.equal(calculateNumber(4.5,4.5), 10);
	});
});