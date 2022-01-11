const calculateNumber = require('./2-calcul_chai');
const chai = require('chai')
const expect = chai.expect;


describe ("Test suite 1 - Sum", function() {
	it("Tests that a and b are rounded properly and return the correct", function() {
		expect(calculateNumber('SUM', 1.1, 1.2)).to.equal(2);
		expect(calculateNumber('SUM', 9.9, 0)).to.equal(10);
		expect(calculateNumber('SUM', 1, 1.6)).to.equal(3);
	});
})

describe ("Test suite 2 - Difference", function () {
	it ("Tests that a and b are rounded and return the proper difference", function () {
		expect(calculateNumber('SUBTRACT', 1.1, 1.2)).to.equal(0);
		expect(calculateNumber('SUBTRACT', 9.9, 5)).to.equal(5);
		expect(calculateNumber('SUBTRACT', 1, -1.1)).to.equal(2);
	});
})

describe ("Test suite 3 - Quotient", function () {
	it ("Tests that a and b are rounded and return the proper quotient", function () {
		expect(calculateNumber('DIVIDE', 1.1, 1.2)).to.equal(1);
		expect(calculateNumber('DIVIDE', 9.9, 5)).to.equal(2);
		expect(calculateNumber('DIVIDE', 1, 1.1)).to.equal(1);
		expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
		expect(calculateNumber('DIVIDE', 1, 0.1)).to.equal('Error');
	});
})