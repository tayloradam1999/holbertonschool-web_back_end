export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  // getter for name
  get name() {
    return this._name;
  }

  // setter for name
  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  // getter for length
  get length() {
    return this._length;
  }

  // setter for length
  set length(newLength) {
    if (typeof newLength === 'number') {
      this._length = newLength;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  // getter for students
  get students() {
    return this._students;
  }

  // setter for students
  set students(newStudents) {
    if (newStudents instanceof Array) {
      if (!(newStudents.each((i) => (typeof i === 'string')))) {
        throw new TypeError('Student name must be a string');
      }
      this._students = newStudents;
    } else {
      throw new TypeError('Students must be an array');
    }
  }
}
