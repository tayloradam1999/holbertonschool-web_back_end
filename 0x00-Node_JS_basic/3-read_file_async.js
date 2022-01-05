const fs = require('fs').promises;

const countStudents = async (path) => {
  let fileData;
  try {
    fileData = await fs.readFile(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }
  // Calculate number of students total in database
  // DOES NOT INCLUDE HEADER LINE OF CSV FILE AND BLANK LINES
  console.log(`Number of students: ${fileData.split('\n').length - 2}`);
  // get list of every unique field value
  const fields = fileData.split('\n').map((line) => line.split(',')[3]);
  // get only unique values
  const uniqueFields = [...new Set(fields)];

  // start looping for students in each field
  // declare dict to populate with num of students in field + list of students
  const dict = {};
  for (let i = 0; i < uniqueFields.length; i += 1) {
    // get number of students in each field
    const studentsInField = fileData.split('\n').filter((line) => line.includes(uniqueFields[i])).length;
    // get list of students in each field
    const studentsInFieldList = fileData.split('\n').filter((line) => line.includes(uniqueFields[i])).map((line) => line.split(',')[0]);
    // add spaces between elements in arrays
    const studentsInFieldListString = studentsInFieldList.join(', ');
    // log
    console.log(`Number of students in ${uniqueFields[i]}: ${studentsInField}. List: ${studentsInFieldListString}`);
    // add to dict
    dict[uniqueFields[i]] = {
      num: studentsInField,
      list: studentsInFieldListString,
    };
  }
  return dict;
};

module.exports = countStudents;
