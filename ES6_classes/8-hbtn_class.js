export default class HolbertonClass {
    constructor(size, location) {
        this._location = location;
        this._size = size;
    }
    [Symbol.toPrimitive](hint) {
        if (typeof hint === Number) {
            return this._size;
        }

        if (typeof hint === String)
            return this._location;
        return this._location;
    }
}
