// Create a Car class with make, model, and year attributes.
// Then create an electric Car class that adds batteryLevel

interface ICar {
    make: string;
    model: string;
    year: number;
    startEngine(): void;
}

class Car implements ICar{
    constructor(
        public make: string,
        public model: string,
        public year: number
    ) {}
    startEngine(): void {
        console.log(`${this.make} ${this.model} is ready to go!`)
    }
}

class ElectricCar extends Car{
    batteryLevel: number

    constructor(
        make: string,
        model: string,
        year: number,
        batteryLevel: number
    ) {
    super(make, model, year);
    this.batteryLevel = batteryLevel;
    }

    startEngine(): void {
        console.log(`Electric Car Online (Battery Level: ${this.batteryLevel}%)`)
    }
}

const myCar = new Car('Honda', 'Civic', 2022);
myCar.startEngine();

const myElectricCar = new ElectricCar('Tesla', 'Model Y', 2024, 89)
myElectricCar.startEngine();