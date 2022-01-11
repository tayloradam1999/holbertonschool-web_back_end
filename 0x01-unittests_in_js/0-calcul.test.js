const calculateNumber = require('./0-calcul')
const assert = require('assert');


describe ("Test suite", function() {
	it("Tests that a and b are rounded properly using Math.round()", function() {
		assert.equal(calculateNumber(1.1, 2.2), 3);
		assert.equal(calculateNumber(1.4, 1,4), 2);
		assert.equal(calculateNumber(1.5, 1.5), 4);
		assert.equal(calculateNumber(1.6, 1.6), 4);
		assert.equal(calculateNumber(1.7, 1), 3);
		assert.equal(calculateNumber(1, 1.8), 3);
		assert.equal(calculateNumber(-5, 0.5), -4);
		assert.equal(calculateNumber(0, -10.98), -11);
		assert.equal(calculateNumber(1.1, 1.9), 3);
		assert.equal(calculateNumber(1.1, 0), 1);
	});
})