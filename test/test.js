class Animal {
    constructor(){
        this.type = 'animal'
    }
    says(text){
        setTimeout(
            ()=>console.log(`${this.type} says ${text}`)
            ,1000)
    }
}
let animal = new Animal()
animal.says('hi')