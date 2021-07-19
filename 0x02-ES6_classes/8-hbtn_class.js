export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // eslint-disable-next-line consistent-return
  [Symbol.toPrimitive](x) {
    if (x === 'number') {
      return this._size;
    } if (x === 'string') {
      return this._location;
    }
  }
}
