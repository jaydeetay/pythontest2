class Greeter {
    greeting: string
    constructor(message: string): Greeter {
        this.greeting = message
    }
    
    public greet() {
        return "Hello, " + this.greeting
    }
    
}

let greeter = new Greeter("world")
basic.forever(function on_forever() {
    
})
