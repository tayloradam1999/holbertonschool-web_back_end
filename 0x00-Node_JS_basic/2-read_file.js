const fs = require('fs');

function countStudents(path) {
  // Reads database file synchronously
  let fileData;
  try {
    fileData = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }
  // Calculate number of students total in database
  // DOES NOT INCLUDE HEADER LINE OF CSV FILE AND BLANK LINES
  console.log(`Number of students: ${fileData.split('\n').length - 2}`);
  // calculate CS fields and SWE fields
  const CS = fileData.split('\n').filter((line) => line.includes('CS')).length;
  const SWE = fileData.split('\n').filter((line) => line.includes('SWE')).length;
  // Put all student names of CS and SWE fields in arrays
  let CSstudents = fileData.split('\n').filter((line) => line.includes('CS')).map((line) => line.split(',')[0]);
  let SWEstudents = fileData.split('\n').filter((line) => line.includes('SWE')).map((line) => line.split(',')[0]);
  // add spaces between elements in arrays
  CSstudents = CSstudents.join(', ');
  SWEstudents = SWEstudents.join(', ');
  // log
  console.log(`Number of students in CS: ${CS}. List: ${CSstudents}`);
  console.log(`Number of students in SWE: ${SWE}. List: ${SWEstudents}`);
}

module.exports = countStudents;
