import Currency from "./3-currency";

export default class Pricing {
    constructor(amount, currency) {
        this._amount = amount;
        this._currency = currency;
    }
    get currency() {
        return this._currency;
    }
    set currency(newcurrency) {
        this._currency = newcurrency;
    }
    get amount() {
        return this._amount;
    }
    set amount(newa) {
        this._amount = newa;
    }
    displayFullPrice() {
        return `${this._amount} ${this._currency.code} (${this._currency.name})`
    }
    static convertPrice(amount, conversionRate) {
        return amount * conversionRate;
    }
}
