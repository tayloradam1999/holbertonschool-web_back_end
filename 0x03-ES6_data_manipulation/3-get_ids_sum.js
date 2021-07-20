export default function getStudentIdsSum(getListStudents) {
  return getListStudents.reduce((accumulator, x) => accumulator + x.id, 0);
}
