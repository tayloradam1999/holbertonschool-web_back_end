export default function createInt8TypedArray(length, position, value) {
  const myAB = new ArrayBuffer(length);
  for (let i = 0; i < position; i += 1) {
    if (i === position) {
      i = value;
    }
  }
  return myAB;
}
