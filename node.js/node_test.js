'use strict'

var fs = require('fs')
var rs = fs.createReadStream('node_test_.js', 'utf-8')

rs.on('data', function (chunk) {
    console.log('Data:')
    console.log(chunk)
})

rs.on('data', function (chunk) {
    console.log('Data: ')
    console.log('xinghang')
})