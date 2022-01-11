const calculateNumber = require('./1-calcul')
const assert = require('assert');


describe ("Test suite", function() {
	it("Tests that a and b are rounded properly using Math.round()", function() {
		assert.equal(calculateNumber('SUM', 1.1, 1.2), 2);
		assert.equal(calculateNumber('SUM', 9.9, 0), 10);
		assert.equal(calculateNumber('SUM', 1, 1.6), 3);
		assert.equal(calculateNumber('SUBTRACT', 1.1, 1.2), 0);
		assert.equal(calculateNumber('SUBTRACT', 9.9, 5), 5);
		assert.equal(calculateNumber('SUBTRACT', 1, -1.1), 2);
		assert.equal(calculateNumber('DIVIDE', 1.1, 1.2), 1);
		assert.equal(calculateNumber('DIVIDE', 9.9, 5), 2);
		assert.equal(calculateNumber('DIVIDE', 1, 1.1), 1);
		assert.equal(calculateNumber('DIVIDE', 1, 0), 'Error');
		assert.equal(calculateNumber('DIVIDE', 1, 0.1), 'Error');
	});
})