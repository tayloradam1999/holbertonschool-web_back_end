export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  // name.getter
  get name() {
    return this._name;
  }

  // name.setter
  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  // length.getter
  get length() {
    return this._length;
  }

  // length.setter
  set length(newLength) {
    if (typeof newLength === 'number') {
      this._length = newLength;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  // students.getter
  get students() {
    return this._students;
  }

  // students.setter
  set students(newStudents) {
    if (newStudents instanceof Array) {
      newStudents.forEach((i) => {
        if (!(typeof i === 'string')) {
          throw new TypeError('Student name must be a string');
        }
      });
      this._students = newStudents;
    } else {
      throw new TypeError('Students must be an array');
    }
  }
}
