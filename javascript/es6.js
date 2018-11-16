关于es6:
// let, const
// class, extends, super
// arrow functions
// template string
// destruction
// function default, rest arguments
// Promise

//var全局作用域
var name = 'xinghang'
while (true) {
    var name = 'feifei'
    console.log(name)//feifei
    break
}
console.log(name)//feifei
//let块作用域
let name = 'xinghang'
while (true) {
    let name = 'feifei'
    console.log(name)//feifei
}
console.log(name)//xinghang
//cont只读
const PI = Math.PI

//class super extends
class Animal {
    constructor() {
        this.palce = 'earth'
        this.type = 'animal'
    }
    says(text) {
        console.log(this.type + ' says '+ text)
    }
}
class Cat extends Animal {
    constructor(){
        super()
        this.type = 'cat'
        this.name= 'kitty'
    }
    talk(text) {
        super.says(text)
        console.log(this.name + ' talk ' + text)
    }
}
cat = new Cat()
console.log(cat.palce)
cat.says('hello')
cat.talk('hello')
// class static methods
class Animals {
    static says (text) {
        console.log(text)
    }
}
Animals.says('something') //something
let animals = new Animals()
animals.says('something') //error

//arrow function
class Animal {
    constructor() {
        this.type = 'animal'
    }
    says(text) {
        setTimeout(function() {
            console.log(this.type + 'says' + text)
        }, 1000)
    }
}
let animal = new Animal()
animal.says('hi')//!报错，此时的this只指向Timeout{}而不是实例

class Animal {
    constructor(){
        this.type = 'animal'
    }
    says(text){
        setTimeout({
            ()=>console.log(`${this.type} says ${text}`)
        },1000)
    }
}
let animal = new Animal()
animal.says('hi')

//template string
//es5 烦人的加号
$('#result').append(
    "There are <b>" + basket.count + "</b>" +
    "items in your backet, congratulations!"
)
//es6
$('#result').append(`
    There are <b>${basket.count}<b> items in your
    backet, congratulations!"
`)

//destruction:
//析构赋值表达式
//es5:
let cat = 'ken'
let dog = 'lili'
let zoo = {cat:cat, dog:dog}
console.log(zoo);
//es6:
let cat = 'ken'
let dog = 'lili'
let zoo = {cat, dog}
console.log(zoo)

let zoo = {cat:'ken', dog:'lili'}
let {cat, dog} = zoo
console.log(cat, dog)

//function default:
function animal(type="cat"){
    console.log(type);
}
animal()

//rest:
function animal(...args){
    console.log(args);
}
animal(a,b,c)

//Promise finally
//先看个需求: 把一个工程中的ajax请求封装起来.
//如果我这样写:
//utils.js内
export default {
    _get(url, params) {
        vue.http.get(url, {params: params}).then(response => {
            console.log('success')
            let res = response.body
            return res
        }, response => {
            console.log('error')
            console.log(response.body)
        })
    }
}
//action.js内
import utils from '../utils.js'
let res = utils._get(url, params)
console.log(res)
console.log('something')
commit('ASDFA', res)
//你会发现打印顺序竟然是这样:
//undifine, something, success
//恍然大悟, 原来这段代码中的异步请求,并没有被等待, 这就是promise的作用了.
//所以我这样写
//utils.js内
export default {
    _get(url, params) {
        var p = new Promise((resolve, reject) {
            vue.http.get(url, {params: params}).then(response => {
                console.log('success')
                let res = response.body
                resolve(res)     //对应then,表示成功状态,将res传递给then
            }, response => {
                console.log('error')
                reject(response) //对应catch, 表示失败状态, 将response传递给catch
            })
        })
        return p                 //一定要记得return
    }
}
//action.js内部
import utils from '../utils.js'
utils._get(url, params).then(res => {
    commit('ASDFA', res)
}).catch(res => {
    console.log(res)
})
//完美的解决了异步通信的问题.
export default {
    _get(url, params) {
        var p = new Promise((resolve, reject) {
            vue.http.get(url, {params: params}).then(response => {
                console.log('success')
                let res = response.body
                resolve(res)
            }, response => {
                console.log('error')
                reject(response)
            })
        })
        return p
    }
}
