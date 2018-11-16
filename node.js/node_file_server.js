'use strict'

var
    fs = require('fs'),
    url = require('url'),
    path = require('path'),
    http = require('http');

var root = path.resolve(process.argv[2] || '.')

console.log('Static root dir: ' + root)

var server = http.Server(function (request, response) {
    var pathname = url.parse(request.url).pathname
    var filepath = path.join(root, pathname)
    fs.stat(filepath, function (err, stats) {
        if (!err && stats.isFile()) {
            console.log('Request Path: ' + request.url)
            response.writeHead(200)
            fs.createReadStream(filepath).pipe(response)
        }
        else {
            console.log('error happened: ' + request.url)
            response.writehead(404)
            response.end('404 not find')
        }
    })
})

server.listen(8080)

console.log('Server is running at http://127.0.0.1:8080/')
