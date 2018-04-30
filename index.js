var parse = require('./parser')
var fs = require('fs')

fs.readFile('waa.todo.txt', 'UTF-8', function(err, data) {
  parse(data)
})
