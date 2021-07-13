export default function appendToEachArrayValue(array, appendString) {
  const arr = [];
  for (const idx of array) {
    const val = appendString + idx;
    arr.push(val);
  }

  return arr;
}
