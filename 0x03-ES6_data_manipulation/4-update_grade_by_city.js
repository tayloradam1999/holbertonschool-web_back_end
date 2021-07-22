/* eslint-disable */
export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  if (!(getListStudents instanceof Array)) {
    return [];
  }

  function doGrading(student) {
    if (student.grade === undefined) {
      student.grade = 'N/A';
    }
    newGrades.forEach((x) => {
      if (x.studentId === student.id) {
        student.grade = x.grade;
      }
    });
    return student;
  }

  const SL = getListStudents.filter((x) => x.location === city);
  return SL.map(doGrading);
}
