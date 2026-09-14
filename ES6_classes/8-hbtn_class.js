export default class HolbertonClass {
    constructor(size, location) {
        this._location = location;
        this._size = size;
    }
    [Symbol.toPrimitive](hint) {
        if (hint === "Number") {
            return this._size;
        }

        if (hint === "String")
            return this._location;
    }
}
