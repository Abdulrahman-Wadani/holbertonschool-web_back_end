export default class Car {
    constructor(brand, motor, color) {
        this._brand = brand;
        this._color = color;
        this._motor = motor;
    }
    cloneCar() {
        return new (Car(this._brand, this._motor, this._color));
    }
}
