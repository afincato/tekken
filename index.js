var parse = require('./parser')
var fs = require('fs')
var process = require('process')
var path = require('path')
var filter = require('./filter')
var views = require('./views')

function read_directory(dir){
    fs.readdir(folder, (err, files) => {
      if (err) throw err

      files
        .filter(file => { return path.extname(file) === '.txt' || path.extname(file) === '.md' })
        .forEach(file => {
          read_file(file)
        })
    })
}

function read_file(file){
    fs.readFile(path.join(folder, file), 'UTF-8', function(err, data) {
      if (err) throw err

      var parse_data = parse(data);
      var filter_data = filter.filter(
        filter.filter(parse_data, filter.wk),
        filter.prune
      )
      views(filter_data, []).forEach(function (line) {
        console.log(line)
      })
      console.log('')
    })
}

function main(){
  var folder = process.argv[2]
  read_directory(folder)
}
