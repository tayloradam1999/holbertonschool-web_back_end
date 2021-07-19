/* eslint-disable class-methods-use-this */
/* eslint-disable import/prefer-default-export */
import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this.floors = floors;
  }

  get floors() {
    return this._floors;
  }

  set floors(MYFLOORS) {
    this._floors = MYFLOORS;
  }

  evacuationWarningMessage() {
    return (`Evacuate slowly the ${this.floors} floors`);
  }
}
