export default function hasValuesFromArray(set, array) {
  const array2 = Array.from(set);
  if (array.every((elem) => array2.includes(elem))) {
    return true;
  }
  return false;
}
