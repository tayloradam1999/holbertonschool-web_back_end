var myClass = require('./0-calcul');
var myObj = new myClass();
var chai = require('chai');
var assert = chai.assert;


describe ("test suite", function() {
	it("Test if adds rounded ints", function () {
		assert(myObj.calculateNumber(1, 2) === 3);
	});
});