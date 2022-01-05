const fs = require('fs');
const util = require('util');

// reads from database file asynchronously
function countStudents(path) {
	try {
		let fileData = util.promisify(fs.readFile)(path, 'utf8');
	} catch (err) {
		throw new Error('Cannot load the database');
	}
	return fileData.then((data) => {
		// Calculate number of students total in database
		// DOES NOT INCLUDE HEADER LINE OF CSV FILE AND BLANK LINES
		console.log(`Number of students: ${data.split('\n').length - 2}`);
		// calculate CS fields and SWE fields
		const CS = data.split('\n').filter((line) => line.includes('CS')).length;
		const SWE = data.split('\n').filter((line) => line.includes('SWE')).length;
		// Put all student names of CS and SWE fields in arrays
		let CSstudents = data.split('\n').filter((line) => line.includes('CS')).map((line) => line.split(',')[0]);
		let SWEstudents = data.split('\n').filter((line) => line.includes('SWE')).map((line) => line.split(',')[0]);
		// add spaces between elements in arrays
		CSstudents = CSstudents.join(', ');
		SWEstudents = SWEstudents.join(', ');
		// log
		console.log(`Number of students in CS: ${CS}. List: ${CSstudents}`);
		console.log(`Number of students in SWE: ${SWE}. List: ${SWEstudents}`);
	});
}