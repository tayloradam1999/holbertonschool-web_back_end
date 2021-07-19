export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  // code.getter
  get code() {
    return this._code;
  }

  // code.setter
  set code(newCode) {
    this._code = newCode;
  }

  // name.getter
  get name() {
    return this._name;
  }

  // name.setter
  set name(newName) {
    this._name = newName;
  }

  displayFullCurrency() {
    return (`${this._name} (${this._code})`);
  }
}
