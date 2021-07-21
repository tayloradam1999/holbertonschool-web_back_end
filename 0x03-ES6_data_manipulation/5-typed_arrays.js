export default function createInt8TypedArray(length, position, value) {
  const myAB = new ArrayBuffer(length);
  const myView = new DataView(myAB, 0);
  const my8Array = new Int8Array(myAB);
  for (let x = 0; x < length; x += 1) {
    if (position > length) {
      throw new Error('Position outside range');
    } if (x === position) {
      my8Array[x] = value;
    }
  }
  return myView;
}
