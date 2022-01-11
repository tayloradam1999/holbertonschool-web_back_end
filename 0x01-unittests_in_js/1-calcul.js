// function to round a and b and return sum

const calculateNumber = (type, a, b) => {
	if (type === '+') {
		return Math.round(a) + Math.round(b);
	} else if (type === '-') {
		return Math.round(a) - Math.round(b);
	} else if (type === '*') {
		return Math.round(a) * Math.round(b);
	} else if (type === '/') {
		return Math.round(a) / Math.round(b);
	}
}

module.exports = calculateNumber;