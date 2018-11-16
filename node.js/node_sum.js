// hello world
console.log('hello world');

// http服务器
var http = require('http')
http.createServer(function (request, response) {
	response.writeHead(200, {'Content-Type': 'text/plain'});
	response.end('Hello World\n');
}).listen(8888);
console.log('Server running at http://127.0.0.1:8888/');

// 关于node.js中的用回调实现异步
// 同步
var fs = require('fs')
var data = fs.readFileSync('input.txt')
console.log(data.toString())
console.log(test)
// 回调函数实现异步
var fs = require('fs')
fs.readFile('input.txt', function (err, data) {
    if (err) return console.error(err)
    console.log(data.toString())
})
console.log('test')

//一个node.js后端调用公共接口,然后返回json的例子:
var http = require('http')
var request = require('request')
var urllib = require('url')
var data

request('http://ip.taobao.com/service/getIpInfo.php?ip=106.75.97.4', function (error, response, body) {
    data = JSON.parse(body)
    console.log(data)
})

http
.createServer(function(req, res){
    var params = urllib.parse(req.url, true)
    if (params.query && params.query.callback) {
        var str =  params.query.callback + '(' + JSON.stringify(data) + ')'
        res.end(str)
    }
    res.end(JSON.stringify(data))
})
.listen(8080)
