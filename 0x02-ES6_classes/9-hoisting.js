export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  get year() {
    return this._year;
  }

  set year(newYear) {
    this._year = newYear;
  }

  get location() {
    return this._location;
  }

  set location(newLocation) {
    this._location = newLocation;
  }
}

const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

export class StudentHolberton {
  constructor(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = HolbertonClass;
  }

  get firstname() {
    return this._firstName;
  }

  set firstname(newFN) {
    this._firstName = newFN;
  }

  get lastname() {
    return this._lastName;
  }

  set lastname(newLN) {
    this._lastName = newLN;
  }

  get holbertonClass() {
    return this.holbertonClass;
  }

  set holbertonClass(newHC) {
    this.HolbertonClass = newHC;
  }

  // eslint-disable-next-line class-methods-use-this
  fullStudentDescription() {
    return `${this._firstName} ${this._lastName} - ${this._holbertonClass.year} - ${this._holbertonClass.location}`;
  }
}

const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

const listOfStudents = [student1, student2, student3, student4, student5];
export const listOfStudents;
