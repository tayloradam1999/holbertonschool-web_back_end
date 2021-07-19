// eslint-disable-next-line no-unused-vars
import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  // amount.getter
  get amount() {
    return this._amount;
  }

  // amount.setter
  set amount(newAmount) {
    this._amount = newAmount;
  }

  // currency.getter
  get currency() {
    return this._currency;
  }

  // currency.setter

  set currency(newCurrency) {
    this._currency = newCurrency;
  }

  displayFullPrice() {
    return (`${this.amount} ${this.currency.displayFullCurrency()}`);
  }

  static convertPrice(amount, conversionRate) {
    return (amount * conversionRate);
  }
}
