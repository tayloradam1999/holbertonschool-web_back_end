export default function getStudentsByLocation(getListStudents, city) {
  const myArray = getListStudents.filter((name) => name.location === city);
  return myArray;
}
