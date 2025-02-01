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



const myCar = new Car('Honda', 'Civic', 2022);
myCar.startEngine();
