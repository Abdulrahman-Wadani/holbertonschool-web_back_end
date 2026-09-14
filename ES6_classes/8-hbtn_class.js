export default class HolbertonClass {
    constructor(size, location) {
        this._location = location;
        this._size = size;
    }
    [Symbol.toPrimitive](hint) {
        if (hint === 'number') {
            return this._size;
        }

        if (hint === 'string')
            return this._location;
    }
}
