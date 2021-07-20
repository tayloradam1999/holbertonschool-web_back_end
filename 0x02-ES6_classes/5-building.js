// eslint-disable-next-line import/prefer-default-export
export default class Building {
  constructor(sqft) {
    this.sqft = sqft;
    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(MYSQFT) {
    this._sqft = MYSQFT;
  }
}
