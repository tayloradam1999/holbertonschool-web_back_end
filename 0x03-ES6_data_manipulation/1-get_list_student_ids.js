export default function getListStudentIds(getListStudents) {
  const myArray = getListStudents.map((x) => x * 1);
  if (!(getListStudents instanceof Array)) {
    return ('[]');
  }
  return (myArray);
}
