class myClass {
	constructor(a, b) {
		this.a = Math.round(a);
		this.b = Math.round(b);
	}

	calculateNumber(a, b) {
		return a + b;
	}
}

module.exports = myClass;
