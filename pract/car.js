// Create two car classes. One Car class that has make, model, and year. Another class that extends Car class with an electric Car version

class Car{
    constructor(make, model, year) {
        this.make = make
        this.model = model
        this.year = year
    }
    startEngine(){
        console.log(`${this.make} ${this.model} has started.`)
    }
}

const myCar = new Car("Toyota", "Camry", 2002);
myCar.startEngine();