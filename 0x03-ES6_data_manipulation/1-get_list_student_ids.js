export default function getListStudentIds(getListStudents) {
  if (!(getListStudents instanceof Array)) {
    return [];
  }
  const myArray = getListStudents.map((x) => x.id);
  return myArray;
}
