export default class Currency {
    constructor(name, code) {
        this._name = name;
        this._code = code;
    }
    displayFullCurrency() {
        return `${this._name} (${this._code})`;
    }
}
