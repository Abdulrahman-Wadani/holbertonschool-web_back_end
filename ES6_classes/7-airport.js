export default class Airport {
    constructor(name, code) {
        this._code = code;
        this._name = name;
    }
    [Symbol.toPrimitive](){
        return this._code;
    }
}
