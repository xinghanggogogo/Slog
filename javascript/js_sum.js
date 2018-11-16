// https://github.com/ecomfe/spec/blob/master/javascript-style-guide.md 百度js编码规范
// 百度js编码规范
// utf8编码, 文件结尾处一个空行, 四个空格缩进, 二元运算符两侧必须有一个空格, 一元运算符与操作对象之间不允许有空格
// 语句结束加; 函数定义结束不加; //可是我一个分号也不想加
// 用作代码块起始的左花括号 { 前必须有一个空格
// if / else / for / while / switch / do / function / try / catch / finally 关键字后，必须有一个空格
// 创建对象时, 属性中的: 之后必须有空格, : 之前不允许有空格
// 函数声明、具名函数表达式、函数调用中, 函数名和 ( 之间不允许有空格
// 在函数调用、函数声明、括号表达式、属性访问 中 if / for / while / switch / catch 等语句中，() 和 [] 内紧贴括号部分不允许有空格
// 单行声明的数组与对象，如果包含元素，{} 和 [] 内紧贴括号部分不允许包含空格
// 每个独立语句结束后必须换行
// 运算符处换行时，运算符必须在新行的行首
// 对于 if...else...、try...catch...finally 等语句，推荐使用在 } 号后添加一个换行的风格，使代码层次结构更清晰，阅读性更好
// eg.
// if (condition) {
//     // some statements;
// }
// else {
//     // some statements;
// }
// 关于命名规则：
// 变量 使用 Camel命名法：var loadingModules = {}
// 常量 使用 全部字母大写，单词间下划线分隔 的命名方式：var HTML_ENTITY = {}
// 函数 函数参数 使用 Camel命名法
// 类 使用 Pascal命名法
// 枚举变量 使用 Pascal命名法，枚举的属性 使用 全部字母大写，单词间下划线分隔 的命名方式
// 函数名 使用 动宾短语：function getStyle(element) {}
// boolean 类型的变量使用 is 或 has 开头：var isReady = True
// Promise对象 用 动宾短语的进行时 表达：var loadingData = new Promise((resolve, reject) {})
// loadingData.then(callback)
// 关于注释：
// 单行//
// 多行/**/
// 文档说明/** */
// /**
//  *@file:
//  *@class:
// */
// 一个函数的说明
// /**
//  * 函数描述
//  *
//  * @param {Object} option 参数描述
//  * @param {string} option.url option项描述
//  * @param {string=} option.method option项描述，可选参数
//  */
// function foo(option) {
//     //Todo
// }
// 使用严格的===避免等于判断中隐式的类型转换，但是有的时候==也是好用的
// 对有序集合进行顺序无关的遍历时，使用逆序遍历：逆序遍历可以节省变量，代码比较优化，
// 关于字符串：
// 单引号, 字符串拼接使用数组和'+', '+'效率更高，而数组兼容老版本的浏览器(['a', 'b', 'c'].join(''))
// split
// 字符转转义，要有印象
// HTML 转义
// var str = '<p>' + htmlEncode(content) + '</p>';
// var str = '<input type="text" value="' + htmlEncode(value) + '">';
// URL 转义
// var str = '<a href="/?key=' + htmlEncode(urlEncode(value)) + '">link</a>';
// JavaScript字符串 转义 + HTML 转义
// var str = '<button onclick="check(\'' + htmlEncode(strLiteral(name)) + '\')">提交</button>';
// 关于object：
// 新建空对象 var obj = {}, 对象属性要么全加'', 要么全不加'', 使用.来访问对象属性
// 关于array：
// 新建空数组 var arr = []
// 清空数组使用 arr.length = 0

//关于js中的内存的分类:
//浏览器加载html文档, 会为js申请两种内存, 栈内存, 堆内存
//栈内存: 用来执行js代码的环境(作用域). js作用域只有两种, 全局作用域, 和私有作用域
//堆内存: 用来存储引用数据类型的内容, Object就是key-value, function就是函数字符串

//array concat, push, join, slice, map, filter, indexOf ,sort
//array concat
var a = ['a']
var b = ['b']
var c = 'c'
console.log(a.concat(b));   //['a', 'b']
console.log(a.concat(c));   //['a', 'b', 'c']

//array join array>str
var a = ['a', 'b', 'c']
console.log(a.join());              //'abc'
console.log(a.join('x'));           //'axbxcx'
//注意同python语法的区别: 'x'.join(['a', 'b'])

//array slice
var a = ['a', 'b', 'c', 'd']
console.log(a.slice(1, 2));  //['b']
console.log(a.slice(1));    //['b','c','d']
console.log(a.slice(-2));   //['c','d']
console.log(a.slice(-1));   //['d']

//array map，array to array
//es6
var test = [1, 2, 3].map(x => x+1)
console.log(test)
var a = state.map(todo => {
        if (todo.id === updatedTodo.id) {
          return { ...todo, ...updatedTodo };
        }
        else {
          return todo;
        }
})
//es5 注意bind
[1, 2, 3].map((function(x){
    return x+1
}).bind(this))
[1, 2, 3].map(function(x){
    return x+1
}.bind(this))
//上边这个例子现在就可以清晰的看懂了: es5的语法, 没有使用箭头函数, 此时this指的是全局window, 必然x未声明, 所以需要绑定this.

//array filter array to array
var a = [1, 2, 3, 4].filter(item => item%2===0)
console.log(a)
//test: 请说明下列代码的报错信息, 并改正:
var a = [1, 2, 3, 5].filter(function(item) {
    return item%2 === 0
})
console.log(a)
//item is not defined; bind(this)

//array push with ajax
$.getJSON('/test', {param1: value1}, function(response) {
    var data = response.data
    var items = []
    $.each(data, function(key, val) {
        //es5:
        items.push('<li id="' + key + '">' + val + '</li>')
        //es6:
        items.push(`<li id=${key}>${val}</li>`)
        $('<ul/>', {class: 'ul-class', html: items.join(',')}).appendTo('<selector>')
    })
})

// 关于js中 num, str, bollen 等基本数据类型的转换:
// num转str, 共三种使用第一种
var num = 1
num = num + ''
num = String(num)
num = num.toString()
// str转num：
var str = '1'
str = +str
str = Number(str)
// str转num，并期望忽略数字后的非数字字符串时使用parseInt(), 使用parseInt(必须指定进制)
var width = '200px'
a = parseInt(width, 10)
// num,str转boolen：!!a
var a = 3.14;
console.log(!!a)         //ture
var b = 0
console.log(!!b)         //false
var c = ''
console.log(!!c)         //false
// num去掉小数点使用Math.round(),不要使用parseInt():
var a = 3.14
console.log(Math.round(a)    //四舍五入
console.log(Math.ceil(a))    //向下取整
console.log(Math.floor(a))   //向上取整
//四舍五入: <float>.toFixed(2) 2是保留位数
console.log((1.2345.toFixed(2))) //js万物皆对象, 什么是对象? 有自己的属性和方法就是对象

//使用for in 的方法来实现数组或者对象的迭代:
//在array中 i 相当于index, 在object中 i 相当于 key
//实质是因为数组(array)和对象(object)都属于Object都是引用数据类型, 以key-value存在于堆内存中,
//数组的key就是1234, 而对象的key是可以定义的
var a = ['a', 'b', 1, 2]
var b = {'a': 1, 3: 'b'}
for (var i in a) {
    console.log(i)
    console.log(a[i])
}
for (var i in b) {
    console.log(i)
    console.log(b[i])
}

//关于js中的预解释
//变量声明的提前规则:
//解析器将当前作用域内所有变量和函数(带var和带function)的声明提前到作用域的开始处
//不同点是, var会仅仅声明, 而function声明, 并定义, 空间存的是字符串
var a = 1
function test() {
    console.log(a)
    var a = 1
}
test() //undefined
//等同于:
var a = 1
function test() {
    var a
    console.log(a)
    a = 1
}
test() //undefined

//关于undefined, null的差别:
//第一问 a is not defined的出现情况(直接使用未声明变量)
console.log(a)     //VM1497:1 Uncaught ReferenceError: a is not defined.
//第二问 出现undefined的情况
//1.使用声明过但未定义, 默认值是undefined
var a
console.log(a)
//2.未声明变量typeof会报undefined
console.log(typeof(a))
//一个相关的面试题:
var a = 1
var a
alert(typeof(a))   //number
(function() {
    b = '-----'
    var b
})()
alert(typeof(b)) //undefined, 作用域不一样, 未声明, 未定义.
//第三问 关于null
a = null
console.log(typeof(a))
//object (null是特殊的object(本质是一个未初始化的指针), {}并不是null, typeof操作会返回"object")
a = {}
onsole.log(a == null)
//false ({}并不是null)
var a = {}
var b = null
a.name = 'xinghang'
b.name = 'feifei' //这里会报错, b为空指针对象, 不能像普通对象一样直接添加属性。
b = a
b.name = 'xinghang'
//此时 a 和 b 指向同一个对象。a.name, b.name 均为'jam'

//js基本数据类型判空的最佳实现
//0, '', boolen
var a = '' or var a = 0 or var a = false
if (!a) {console.log('success')}
//注意下面这个例子:
//数组去重
function test(arr) {
    var dic = {}
    var res = []
    for (i in arr) {
        if (!dic[arr[i]]) {
            dic[arr[i]] = 1
            res.push(arr[i])
        }
    }
    return res
}
var a = ['a', 'b', 'ac', 'a', 1, 1, 2]
console.log(test(a))

//js引用数据类型判空的最佳实现
//关于array判空
a = []
if (!a.length) {console.log('success')}
//关于object判空:
//自定义方法
function IsEmpty(obj) {
    for (var i in obj) {
        return false
    }
    return true
}
var a = {}
a.name = 'something'
console.log(isEmpty(a))        //false
console.log(isEmpty({}))       //true
console.log(isEmpty(null))     //true
//jquery自带方法
console.log(isEmptyObject({})) //true


//迭代数组的最佳方案：
//对有序集合进行顺序无关的遍历时, 使用逆序遍历: 逆序遍历可以节省变量, 代码比较优化
var a = ['a', 'b', 'c', 1, 2]
aLen = a.length
while (aLen--) {
    console.log(a[aLen])
}

//对$()的理解
$('#id').click() //表示选择器
$(this).text('something')
$(document).ready()//表示文档加载完成，一般简写为：
$(function () {
    console.log('something')
})
//对于一个标准的js文件的结构，可以这样写
$(function () {
    var app = {
        a: 1,
        test() {
            console.log(this.a)
        }
    }
    $('#someid').on('click', app.test())
})
$(function () {
    var app = {
        a: 1,
        b() {
            console.log(this.a);
        },
    }
    $('#someid').on('click', app.test())
})

//关于js计时器
//html
<button id='my-button'>120</button>
//js
$('button').on('click', function() {
    $('button').attr('disabled', true)
    var totalTime = +$('button').text()
    var timer = setInterval(function() {
        $('button').text(--totalTime)
        if(totalTime <= 0) {
            $('button').attr('disabled', false)
            $('button').text(120)
            clearInterval(timer);
        }
    }, 1000)
})

//js Object's api
//constructor(属性), hasOwnProperty, keys, values
//判断类型
console.log({}.constructor === Object)
console.log([].constructor === Array)
//拥有属性
var x = {foo: 'something'}
console.log(x.hasOwnProperty('foo'))
//keys or values to array,
//IE8及以下是不支持的!
var a = {x: 1, y: 2}
var keys_arr = Object.keys(a)
var values_arr = Object.values(a)
//or
var pt = {x: 1, y: 2, z: 'xing'};
console.log(pt);
var keys_arr = []
var values_arr = []
for (i in pt) {
    keys_arr.push(i)
    values_arr.push(pt[i])
}
console.log(keys_arr, values_arr)
//or这里失效了！concat失效了！
var pt = {x: 1, y: 2, z: 'xing'}
console.log(pt)
var keys_arr = []
var values_arr = []
for (i in pt) {
    keys_arr.push(i)
    values_arr.cancat(String(pt[i]))
}
console.log(keys_arr, values_arr)
//把一个object的所有value or key拼成字符串,
var pt = { x: 1, y: 2, z: 'xing' }
console.log(pt);
var keys_str = ''
var values_str = ''
for (i in pt) {
    keys_str += i + ''
    values_str += pt[i] + ''
}
console.log(keys_str, values_str);

//编写一个数组去重的方法:
//利用array的indexOf方法, 不在array中, 返回-1
//way1
function test(arr) {
    var res = []
    for (var i=0, len=arr.length; i<len; i++ ) {
        if (res.indexOf(arr[i]) == -1) {
            res.push(arr[i])
        }
    }
    return res
}
var a = ['a', 'b', 'ac', 'a', 1, 1, 2]
console.log(test(a))
//way1.5
function test(arr) {
    var res = []
    for (var i in arr) {
        if (res.indexOf(arr[i]) == -1) {
            res.push(arr[i])
        }
    }
    return res
}
var a = ['a', 'b', 'ac', 'a', 1, 1, 2]
console.log(test(a))
//way2 报错原因未知
function test(arr) {
    var dic = {}
    var res = []
    for (i in arr) {
        if (!dic.arr[i]) {
            dic.arr[i] = 1
            res.push(arr[i])
        }
    }
    return res
｝
var a = ['a', 'b', 'ac', 'a', 1, 1, 2]
console.log(test(a))
//way2.5 成功
function test(arr) {
    var dic = {}
    var res = []
    for (i in arr) {
        if (!dic[arr[i]]) {
            dic[arr[i]] = 1
            res.push(arr[i])
        }
    }
    return res
}
var a = ['a', 'b', 'ac', 'a', 1, 1, 2]
console.log(test(a))
//way3 这种方法效率最高可是破坏了原数组的顺序
//空间复杂度最优
function test(arr) {
    var tmp = arr.sort()
    var key = 1
    for (var i=1, len=tmp.length; i<len; i++) {
            if (tmp[i] != tmp[i-1]) {
                tmp[key] = tmp[i]
                key++
            }
    }
    return tmp.slice(0, key)
}
var a = ['a', 'b', 'ac', 'a', 1, 1, 2]
console.log(test(a))

//js快速排序的递归写法, 两层while (start<end)必须都有, 否则控制台卡死
if (typeof Array.prototype.quickSort !== 'function') {
    Array.prototype.quickSort = function () {
        quickSortHelper(this, 0, this.length-1);
        function quickSortHelper(arr, start, end) {
            if(start < end){
                var part = partation(arr, start, end)
                arguments.callee(arr, start, part - 1)
                arguments.callee(arr, part + 1, end)
            }
        }
        function partation(arr, start, end) {
            var pivot = arr[start]
            while (start < end) {
                while (start < end && arr[end] > pivot) {
                    end -= 1
                }
                arr[start] = arr[end]
                while(start < end && arr[start] < pivot) {
                    start += 1
                }
                arr[end] = arr[start]
            }
            arr[start] = pivot
            return start
        }
    }
}
var arr = [5, 2, 3, 1, 4]
arr.quickSort()
console.log(arr)
//简洁版的js快排
function quickSort(seq, low, high) {
    if (low < high) {
        console.log(seq)
        pivot = partition(seq, low, high)
        quickSort(seq, low, pivot-1)
        quickSort(seq, pivot+1, high)
    }
}
function partition(seq, low, high) {
    tmp = seq[low]
    while (low < high) {
        while (low < high && seq[high] >= tmp) {
            high--
        }
        seq[low] = seq[high]
        while (low < high && seq[low] < tmp) {
            low++
        }
        seq[high] = seq[low]
    }
    seq[low] = tmp
    return low
}
var seq = [8, 2, 3, 1, 4, 5, 7, 6]
quickSort(seq, 0, seq.length-1)
console.log(seq)

//关于call和apply
//用来方便的实现方法的继承
//对比es6中class extend的区别
//call()的第一个参数是上下文(指定this),后续是实例传入的参数序列
//apply()和call()一个意思, apply()函数有两个参数：第一个参数是上下文(指定this),第二个参数是参数组成的数组。如果上下文是null，则使用全局对象代替
function Animal(name){
    this.name = name;
    this.showName = function(){
        alert(this.name)
    }
}
function Cat(name){
    Animal.call(this, name)
}
var cat = new Cat("Black Cat")
cat.showName()
//多重继承 es5的写法
function Class10(a, b) {
    this.a = a
    this.b = b
    this.showSub = function() {
        alert(this.a - this.b)
    }
}
function Class11(a, b) {
    this.a = a
    this.b = b
    this.showAdd = function () {
        alert(this.a + this.b)
    }
}
function Class2(a, b) {
    Class10.call(this, a, b)
    Class11.call(this, a, b)
}
test = new Class2(2, 1)
test.showSub()
test.showAdd()
//这样就不行了...
function Class10(a, b) {
    this.showSub = function() {
        alert(this.a - this.b)
    }
}
function Class11(a, b) {
    this.showAdd = function () {
        alert(this.a + this.b)
    }
}
function Class2(a, b) {
    Class10.call(this, a, b);
    Class11.call(this, a, b);
}
test = new Class2(2, 1)
test.showSub()      //NaN
test.showAdd()      //NaN
//es6的写法
function Class10(a, b) {
    this.showSub = () => {
        alert(a - b)
    }
}
function Class11(a, b) {
    this.showAdd = () => {
        alert(a + b)
    }
}
function Class2(a, b) {
    Class10.call(this, a, b);
    Class11.call(this, a, b);
}
test = new Class2(2, 1)
test.showSub()
test.showAdd()
function Class2(a, b) {
    Class10.call(this, a, b)
    Class10.call(this, a, b)
}

//分别用es5和es6实现方法的继承:
//es5:
function Animal(name){
    this.name = name;
    this.showName = function(){
        alert(this.name)
    }
}
function Cat(name){
    Animal.call(this, name)
}
var cat = new Cat("Black Cat")
cat.showName()
//es6:
class Animal {
    constructor() {
        this.palce = 'earth'
        this.type = 'animal'
    }
    says(text) {
        console.log(this.type + ' says '+ text)
    }
    static go(text) {
        console.log(this.type + ' static says ' + text)
    }
}
class Cat extends Animal {
    constructor(){
        super()
        this.type = 'cat'
        this.name = 'kitty'
    }
    talk(text) {
        super.says(text)
        console.log(this.name + ' talk ' + text)
    }
}
cat = new Cat()
console.log(cat.palce);
cat.says('hello')
cat.talk('hello')
cat.go('hello')
Animal.go('hello')

//js获取浏览器相关信息, navigator
//appName, appVersion, appCodeName, userAgent
function whatBrowser() {
    let appName =  navigator.appName;
    let version = navigator.appVersion;
    let codeName = navigator.appCodeName;
    let userAgent = navigator.userAgent;
    console.log(appName)
    console.log(version)
    console.log(codeName)
    console.log(userAgent)
}
whatBrowser()
// Netscape
// 5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
// Mozilla
// Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36

//关于浏览器的渲染机制
//JS 一定要放在 Body 的最底部么?
//script标签的位置会影响首屏时间么？
//答案是：不影响（如果这里的首屏指的是页面从白板变成网页画面——也就是第一次Painting,这个时间仅仅取决于render完成的时间, 而render是有前提的, 就是整个文档加载完成
//所以无论js代码放在那里, 此时都已经加载完毕了, 但放在body内部有可能截断首屏的内容，使其只显示上面一部分(打断了深度遍历)
//浏览器是逐行加载html文档的, html代码加载成dom树, css代码加载成cssdom树, js代码在加载完成后立即执行, 全部加载完成后, layout, render
//某些js代码是必须放在body前边的, 比如获取浏览器的UA来决定引入不同的css
//但是某些包含dom操作的js代码, 会因为dom树木当前还没有加载完成,导致代码并没有产生效果,这类js代码就应该放在body之后,等待dom树生成之后再加载然后执行
//当然你的js代码还可以放在body中, 但是必须注意,如果这段代码包含了某些dom操作, 它可能会打断dom树的深度遍历, 影响dom树的生成, 导致渲染失败
//所以js代码通常放在body之后

//关于闭包
//闭包是一个概念
//在js中, 一个函数可以访问到函数外部定义的变量, 可是外部却无法访问到函数内部定义的变量,
//为了访问到函数内部定义的变量, 且保证这个变量不被稀释掉, 这就是闭包的作用
//定义一个函数, 在这个函数中定义一个函数并返回它, 内部的定义函数操作变量
//一个最简单直接的闭包的例子
function a() {
    var n = 0
    function res() {
        n++
        console.log(n)
    }
    return res
}
var b = a()
b()     //1
b()     //2
//三个易错的demo
//demo1
for (var i = 0; i < 10; i++) {
    setTimeout(function() {
        console.log(i);
    }, 1000);
}//10个10
for (var i = 0; i < 10; i++) {
    console.log(i)
}//1,2,3....
for (var i = 0; i < 10; i++) {
    (function (e) {
        setTimeout(function () {
            console.log(e)
        }, 1000)
    })(i)
}//1,2,3...这就叫加了一层闭包
//demo2 http://blog.csdn.net/gaoshanwudi/article/details/7355794
//demo3
function a() {
    var result = [];
    for (var i=0; i<10; i++) {
        result[i] = function () {
            return i;
        };
    }
    return result;
}
var b = a()
for (var i=0; i<b.length; i++){
    console.log(b[i]())
}
//用闭包的方式解决demo3
function a() {
    var result = []
    for (var i=0; i<10; i++) {
        (function (e) {
            result[e] = function () {
                return e
            }
        })(i)
    }
    return result
}
var b = a()
for (var i=0; i<b.length; i++) {
    console.log(b[i]());
}

//关于js事件冒泡和事件捕获
//一个直接的发生事件冒泡和捕获的例子:
//html
<body>
    <div>
        <button type="button" id="button2">button1</button>
        <button type="button" id="clickMe">button2</button>
    </div>
</body>
//js
$(function(){
    $('#clickMe').click(function(){
        alert('hello')
    })
    $('body').click(function(){
        alert('baby')
    })
})
//事件冒泡, 当点击button2时,依次弹出hello baby,事件从子节点蔓延到父节点,触发了绑定在父节点的事件,就叫做事件冒泡
//事件捕获, 当点击任意位置, 会弹出baby, 这就叫事件捕获, 通过事件的选择器可以避免发生意料之外的事件捕获
//从内向外冒泡, 然后从外到内捕获
//如何解决冒泡:
//demo1 return false方法
$('#clickMe').on('click', function () {
    alert('hello')
    return false
})
//demo2 ie e.stopPropagation, 非ie cancelBubble
$('#clickMe').click(function (event) {
    alert('hello')
    var e = window.event || event;
    if (e.stopPropagation){
        e.stopPropagation()                   //如果提供了事件对象，则这是一个非IE浏览器
    }
    else{
        window.event.cancelBubble = true     //兼容IE的方式来取消事件冒泡
    }
})

//0.JavaScript特殊数据类型:
//对象(object), 带有属性和方法的特殊数据类型
//JavaScript 中的所有事物都是对象: Number, Sting, undefined, null, object, function
//此外，JavaScript 允许自定义对象
//1.JavaScript一般数据类型:
//基本数据类型: Number, String, Boolean, undefined, null
//引用数据类型: 1.object: {}(对象(Object)), [](Array), RegExp, Date
//            2.function
//基本数据类型操作的值本身,而引用数据类型操作的引用地址, 特别注意, fn变量本身存储的是一个内存地址, 这个地址指定的内存区域里存储的是这个函数定义的内容,是字符串.
//eg.
var a = 12
var obj = {}
function fn() {
    console.log('test1')
}
console.log('test2')
console.log(a)
console.log(obj)
console.log(fn)
console.log(fn()) //fn会先执行.
//2.javascript的本地对象，内置对象和宿主对象:
//本地对象为 Num, Object, Array, Date, RegExp, Number等可以实例化的对象
//内置对象为 Math等不可以实例化的, 可以直接使用其属性的对象
//宿主为浏览器自带的document, window, navigator等
//3.new 操作符具体干了什么:
//创建一个空对象, 继承了new对象(可以是一个已定义的funtion, 比如 var a = new function a() {}, 也可以是关键字比如Array)的属性和方法, 然后返回this
var obj = {}
obj.__proto__ = Base.prototype;
Base.call(obj)

//关于正则表达式
//正则表达式的预定义(分为名词和量词)
//名词:
/*
.       .                   匹配除换行符之外的任何一个字符
\d    [0-9]                 匹配数字
\D    [^0-9]                匹配非数字字符
\s    [\n\r\t\f\x0B]        匹配一个空白字符 //n换行;r行首;t指标;x0Btab
\S    [^\n\r\t\f\x0B]       匹配一个非空白字符
\w    [a-zA-Z0-9_]          匹配字母数字和下划线
\W    [^a-zA-Z0-9_]         匹配除字母数字下划线之外的字符
量词(以下都是贪婪量词, 即力求可以实现的最大匹配):
*     匹配前面的子表达式零次或多次。zo* 能匹配 "z" 以及 "zoo"。 * 等价于{0,}。
+     匹配前面的子表达式一次或多次。'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。
?     匹配前面的子表达式零次或一次。"do(es)?" 可以匹配 "do" 或 "does" 中的"do" 。? 等价于 {0,1}。
[a-z] 匹配内部的任意子表达式。
{n}   n 是一个非负整数。匹配确定的n次。'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。
{n,}  n 是一个非负整数。至少匹配n次。'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。
{n,m} m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。 "o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。
用贪婪量词进行匹配时叫做贪婪匹配, 即力争最大匹配, 以上量词都是贪婪量词
用惰性量词进行匹配时, 贪婪量词后加?变成惰性匹配, 即力争最小匹配
var str = "abc";
var re = /\w+/;//将匹配abc
re = /\w+?/;//将匹配a
*/
//js正则表达式RegExp
//js两种表达式的方式你知道吗?1:var re = /\d+/ig, 2, var re = new RegExp('\d+', 'ig'))
//完整清晰的正则表达式教程见 http://www.cnblogs.com/aaronjs/archive/2012/06/30/2570970.html
//test 返回值boolen
//银行卡位数验证正则:
var res = (/^\d{6,}$/).test(vaule)
//手机号正则匹配:
var res = (/^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/).test(value)
//邮箱正则匹配:(注意.的转义符)
var res = (/^[0-9a-zA-Z-_]+@[0-9a-zA-Z-_]+\.[0-9a-zA-Z-_]+$/).test(value)
//replace
var str ="some money"
alert(str.replace("some","much"))       //much money
var re = /\s/
alert(str.replace(re,"%"))              //some%money
str ="some some         some"
re = /\s+/                              //只有一次
alert(str.replace(re,"#"))              //some#some        some
re = /\s+/g;                            //g,全局标志,将使正则表达式匹配整个字符串
alert(str.replace(re,"@"))              //some@some@some@
//split var to array, split后竟然可以跟正则表达式...
var str = "a-bd-c"
var arr = str.split("-")                //["a","bd","c"]
re=/[^a-z]/i                            //前面我们说^表示字符开始,但在[]里它表示一个负字符集,表示非.
arr = str.split(re)                     //仍返回["a","bd","c"];
//search  返回num 在字符串中查找时我们常用indexOf, 只能返回第一个匹配到的
var str = "My age is 18.Golden age!"
re = /\d+/;
console.log(str.search(re));//10
var str = "My age is 18.Golden age!11"
re = /\d+/g;
console.log(str.search(re));//10
//match 返回一个array
//另:这里的一个坑,关于正则中^$的用法(https://zhidao.baidu.com/question/581570451.html)
var str = 'My age is 18.Golden age!, 123, 123'
var res1 = str.match(/^\d+$/)          //null
var res3 = str.match(/\d+/ig)          //["18", "123", "123"]
//replace, 返回一个新的字符串
//利用repalce取cookie的指定值:可以延伸为截取某字符串
//取出指定cookie
cookies = document.cookie
cookieA = cookies.repalce(/.*cookieA=([^;]*).*/, "$1")
//eg2.加粗所有数字
var str = 'asdf123qwer456jkl789'
var reg = /(\d+)/g
str = str.replace(reg, ($1) => `<em>${$1}</em>`)
console.log(str)
//利用正则表达式将url的请求参数转化为字典对象: var reg = /([^&?=]+)=([^&?=]*)/g
//way1
function getQueryObject(url) {
    url = !url ? window.location.href : url;
    var search = url.substring(url.lastIndexOf("?") + 1);  //str.substring(index1,  index2) 字符串截取,只有一个参数时截取至尾部
    var obj = {};
    var reg = /([^?&=]+)=([^?&=]*)/g        //正则的分组, 后续可以用$1获取完全匹配, $2表示第一个分部, $3表示第二个分部,这是replace的特殊用法, 注意同下面的way1对比, 到底谁是$1
    search.replace(reg, ($1, $2, $3) => {
        console.log($1)
        console.log($2)
        console.log($3)
        obj[$2] = $3
    });
    return obj;
}
getQueryObject()
//way2
function getQueryObject(url) {
    url = !url ? window.location.href : url;
    var search = url.substring(url.lastIndexOf('?') + 1)
    var reg = /([^?&=]+)=([^?&=]*)/g
    var a = search.match(reg)
    console.log(a)
    data = {}
    for (i in a) {
        key_value = a[i].split('=')
        data[key_value[0]] = key_value[1]
    }
    console.log(data)
}
getQueryObject()
//获取url中的某个参数
//注:为什么不使用var reg = //的形式呢?因为//这种定义方式我并没有找到方法传递字符串!
//way1
function getParam(param) {
    var url = 'http://xiaomi.com/?id=1&type=2'
    reg = new RegExp('.*'+param+'='+'([^&]*)'+'.*', 'ig')  //i不区分大小写, g全文搜索
    val = url.replace(reg, '$1')
    return val
}
var id = getParam('id')
var type = getParam('type')
console.log(id, type)
//way2
function getParam(param) {
    var url = 'http://xiaomi.com/?id=1'
    reg = new RegExp(param+'='+'([^&]*)', 'ig')  //i不区分大小写, g全文搜索
    var val = url.match(reg)[0]
    return val.split('=')[1]
}
var id = getParam('id')
console.log(id)
//写出'www.bitland.com'的正则
//一个最简单的面试题
var reg = /^w{3}\.\w+\.\w+$/
//将字符串中的所有的数字加上<em>标签
var str = 'asdf123qwer456jkl789'
var reg = /(\d+)/g
str = str.replace(reg, ($1) => `<em>${$1}</em>`)
console.log(str)
//字符串去掉空格
//去除所有, 两头, 左, 右空格:
str = str.replace(/\s+/g, '')
str = str.replace(/^\s+|\s+$/g, '')
str = str.replace( /^\s*/, '')
str = str.replace(/(\s*$)/g, '')
//or juquery自带方法

//根据请求端是否是手机端来判断跳转:
if (!navigator.userAgent.match(/(iPhone|iPod|Android|ios)/i)) {
    window.location.href = "wow.html" //相对路径
}
//一次工作的es6实践, 判断客户端类型:
$(function () {
    if (navinator.userAgent.match(/(iPhone|Android|iPod|ios)/i)) {
        $('.navi;').hide()
    }
    $.post('/stat/new', {}, function (data) {
        all = data.all
        $('#all').append(
            all.map(x => `<td>${x}</td>`).join('')
        )
    $('.pos_follow_ktv_ids').each(
        ktv_id = $(this).attr('data-ktvid')
        var that = $(this)
        $.get('/stat/following', {ktv_id = ktv_id}, function (data) {
            that.text(data.res)
        })
    )
    })
})

//window.location获取url各项参数:
//假设当前的url为: http://101.254.157.124:8888/index.html
window.location.href = 'http://101.254.157.124:8888/index?param=value'
window.location.protocal = 'http:'
window.location.hostname = '101.254.157.124:8888'
window.location.host = '101.254.157.124'
window.location.port = ':8888'
window.location.pathname = '/index'
window.location.search = '?param=value'

//使用em为单位的基础构建代码
//但一个匿名函数被括起来,并且后边再加上一个括号,它就能自动执行.
(function () {
    function size () {
        var winW = document.documentElement.clientWidth || document.body.clientWidth
        document.documentElement.style.fontSize = winw / 10 + 'px';
    }
    size()
    window.onresize = function () {
        size()
    }
})()

//原生js dom操作 last
//访问:
document.getElementById()
document.getElementsByClassName()
document.getElementsByTagName()
document.getElementsByName() // 注: 通过元素的Name属性的值(IE容错能力较强，会得到一个数组，其中包括id等于name值的)
//修改:
document.getElementById("p1").innerHTML = "some_new_text"
document.getElementById("p2").style.color = "blue"
document.getElementById("p3").src = 'http://www.baidu.com'
//新建 添加 删除:
var p = document.createElement("p")
var node = document.createTextNode("这是新段落")
p.appendChild(node)
var element=document.getElementById("div1")
element.appendChild(p);
element.removeChild(p)
//监听事件:(注意是'=')
document.getElementById('intro').onclick = () => {console.log('test')}
//触发事件:
document.getElementById('intro').click()
document.getElementById('input').focus()

// 使用document.cookie和window.localStorage实现页面通信
// 关于cookie:
// 各种后端框架都方便的封装了设置cookie的方法,比如(tonador), 本质上都是通过在响应报文的头部加入Set-Cookie字段来设置的, 形如:
// Set-Cookie: NAME=VALUE; expires=DATE; path=PATH; domain=DOMAIN
// expires是过期时间戳, 通常用当前时间的毫秒数加上一段时间： new Date().getTime()+30*24*60*60*1000)(这就能解释清理cookie的时候, 将expire设置成一个过去的时间就能删除cookie)
// 如果不设置expires, 在浏览器中这个cookie将被当做session对待, 也就是关闭了浏览器cookie就消失(注意在tornado中的用法, 不设置过期时间关闭浏览器cookie就会消失.)
// 读取:
var cookies = document.cookie //这一个分号分隔的包含所有cookie键值字符串，可以通过正则表达式来提取需要的cookie)
var cookieA = cookies.repalce(/.*cookieA=([^;]*).*/, '$1')
console.log(cookieA)
// 设置:
document.cookie = 'cookie_example=123'+';expires='+expire+';path=/';
// 关于localStorage:
// 来自html5, 实现本地存储, 突破了cookie 4k的限制, 最大的存储空间是5M, localStorage中所有的item都是str类型
// 用法:setItem(), getItem(), removeItem()
var storage = window.localStorage
var data = {
    name: 'xinghang',
    sex: 'man',
    hobby: 'program'
}
var dataStr = JSON.stringify(data)
storage.setItem('data', dataStr)
var dataStr = storage.getItem('data')
var dataJson = JSON.parse(dataStr)
console.log(dataJson, typeof(dataJson))
storage.removeItem('data')

// 关于js原生XMLHttpRequest:
var xmlhttp = new XMLHttpRequest()
xmlhttp.onreadystatechange = () => {
    document.getElementById('A1').innerHTML=xmlhttp.status;
    document.getElementById('A2').innerHTML=xmlhttp.statusText;
    document.getElementById('A3').innerHTML=xmlhttp.responseText;
}
xmlhttp.open("GET",url,true)
xmlhttp.send(null)

// 关于js严格模式的一些限制:(use strict)
// 消除JavaScript语法的一些不合理，不严谨，减少一些怪异行为
// 1.全局变量必须显式声明
// 2.禁止this指向全局对象(构造函数，必须加new)
// 3.函数不能有重复的形参名
// 4.保留字(let、interface、package、private、protected、public、static、yield、implements)

// 关于js的作用域以及作用域链:
// js作用域的范围是函数, 函数嵌套函数, 查找变量从内层函数依次向外层找, 最后找不到在window上找

// 关于this
// this是JavaScript的一个关键字, 它只可能存在于函数中, 随着函数使用场合的不同, this的值会发生变化
// 但是有一个总原则, 那就是this指的是调用函数的那个对象, 而鉴于JS所谓的“万物皆对象”, 这个this因此可以是任何物件, 甚至的数字字面值
// When a function of an object was called, the object will be passed into the execution context as 'this' value
// this出现的情景:
// 1.全局范围内:
// this
// 当在全部范围内使用 this, 它将会指向全局对象, 浏览器中运行的 JavaScript脚本, 这个全局对象是window。
// 2.函数调用
// foo()
// 这里 this 也会指向全局对象, 比如下面的eg2
// ES5 注意: 在严格模式下（strict mode），不存在全局变量。 这种情况下 this 将会是 undefined。
// 3.方法调用
// test.foo()
// 这个例子中, this 指向 test 对象
// 4.调用构造函数
// new foo();
// 如果函数倾向于和 new 关键词一块使用, 则我们称这个函数是构造函数, 在函数内部, this指向新创建的对象。
// 5.显式的设置 this
// 比如call和apply函数

//模板引擎的快速使用(type, id, {%%}, 分行, =, 两个参数)
<script type="text/template" id="temp">
    <%for (var i in data) {%>
        <li><%= data[i] %></li>
    <%}%>
</script>
var data = ['a', 'b', 'c']
var html = baidu.template('temp', {data: data})
$('#result').html(html)

//关于react es6中的函数绑定及其延伸
//一个stackoverflow的问题:http://stackoverflow.com/questions/43568344/typeerror-cannot-read-property-function-name-of-undefined-when-binding-onclic
//注意这个问题有四种解决:1.constructor绑定 2.constructor es7绑定 3.直接把函数定义成箭头函数 4.调用函数时传递this 5.答案的最后一句话也是一种方法, 可以衡量你时候真正的理解了this
//当浏览器渲染这个组件的时候, 执行到map函数, 此时的this指的是全局, 必然没有例子中的函数
//然后发现了这个问题:http://stackoverflow.com/questions/32317154/uncaught-typeerror-cannot-read-property-setstate-of-undefined?rq=1
//所以es6中函数绑定的意义非常重要, 使指定函数的this永远不变, 在react es6组件写法的例子中, 调用构建函数, this就永远指向了组件本身
//最后看一下当你绑定函数的时候, bind函数具体做了什么呢: http://blog.csdn.net/jutal_ljt/article/details/53381670
//eg1:
this.x = 'a'
var module = {
    x: 'b',
    getX() {
        return this.x
    }
}
module.getX()
var newGetX = module.getX
newGetX()
//eg2:
function A(a) {
    this.x = a
    var get = function() {
        return this.x
    }
    this.print = function() {
        console.log(get())
    }
}
//如果函数倾向于和new关键词一块使用, 则我们称这个函数是构造函数.在函数内部, this 指向新创建的对象
a = new A(1)
a.print()
//错误原因: 此时get里的this指向的是window(函数)
//改正方法:
//way1:
var that = this
var get = function() {
    return that.x
}
//way2:
var get = function() {
    return this.x
}.bind(this)
//eg3再来看看当初一个例子,你认为是坑, 其实你自己理解不到位的一个例子:
$('.sp_follow_ktv_id').each(function () {
    ktv_id = $(this).attr('data-ktvid')
    $.get('/stat/following', {ktv_id:ktv_id, tp:'sp'}, function (data) {
        this.text(data.res)
    })
})
//应该改成:
$('.sp_follow_ktv_id').each(function () {
    var that = $(this);
    ktv_id = that.attr('data-ktvid')
    $.get('/stat/following', {ktv_id:ktv_id, tp:'sp'}, function (data) {
        that.text(data.res)
    })
})
//or
$('.sp_follow_ktv_id').each(function () {
    ktv_id = $(this).attr('data-ktvid')
    $.get('/stat/following', {ktv_id:ktv_id, tp:'sp'}, function (data) {
        this.text(data.res)
    }).bind(this)
})

//浏览器前进后退配合ajax
//关于window.history.replaceState, window.history.pushState, window.addEventListener("popstate", function() {})
//关于参数: 第一个参数是记录绑定的数据, 第二个参数是标题(很多浏览器都忽略了)，第三个参数是新的URL
//效果如此(http://www.zhangxinxu.com/study/201306/ajax-page-html5-history-api.html?area=pudong)
//第一次进入页面:
window.onload = function() {
    window.history.replaceState({uri: '/test1'}, 'test1', '?key1=value1')
    $.get('/test1', function(data) {
    })
}
//点击侧边栏:(先入state, 再ajax渲染dom)
window.history.pushState({uri: '/test2'}, 'test2', '?key2=value2')
$.get('test2', function(data) {
})
//监听前进后退事件:
window.addEventListener('popstate', function(e) {
    if (history.state) {
        uri = e.state.uri     //注意带上state
        $.get(uri, function(data) {
        })
    }
})

//关于js中的__proto__, prototype, 原型继承, 以及原型链:
//js中万物皆对象, 每个对象都具有__proto__属性, 称为隐式原型, 其值可能是, Num, String, Array, Object, function, 一个对象的隐式原型指向构造该对象的构造函数的原型.
//这也保证了实例能够访问在构造函数的原型中定义的属性和方法.
//js中有两种引用数据类型, 分别是function和object
//对于fucniotn而言, 除了__proto__属性, 还有prototype属性, 这是一个指针, 必然是一个Object
//eg1
var a = 0, '', [], {}
console.log(a.__proto__) //Num, String, Array, Object
console.log(typeof(a.__proto__)) //object
//eg2
var a = function () {}
console.log(a.__proto__) //function
console.log(typeof(a.__proto__)) //function
//eg3
var b = {name: 'test'}
a = Object.create(b)
console.log(a.__proto__) //Object {name: "test"}
//eg4
a = function(){}
console.log(a.prototype) //Object
console.log(typeof(a.prototype)) // object
a.prototype.say = function () {console.log('bingo')}
//eg5
var a = function () {}
var b = new a()
console.log(b.__proto__) //object
b.say()
//输出: bingo
//本质其实是:
var b = {}
b.__proto__ = a.prototype
a.call(b)
//关于原型链
//每个对象都会在其内部初始化一个属性, 就是__proto__, 当我们访问一个对象的属性时, 如果这个对象内部不存在这个属性, 那么他就会去__proto__(引用)里找这个属性
//这个__proto__所指的object也有自己的__proto__, 于是就这样一直找下去, 也就是我们平时所说的原型链的概念
//eg1: https://www.zhihu.com/question/34158992?sort=created
var animal = function () {}
var dog = function () {}
animal.price = 100
dog.prototype = animal
JB = new dog()
console.log(dog.price)  //undefined
console.log(JB.price)   //100
//new 操作符具体干了什么:
//创建一个空对象, 继承了new对象(可以是一个已定义的funtion, 比如 var a = new function a() {}, 也可以是关键字比如Array)的属性和方法, 然后返回this
var JB = {}
JB.__proto__ = dog.prototype;
Base.call(obj)
