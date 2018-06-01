var parse = require('./parser')
var fs = require('fs')
var process = require('process')
var path = require('path')
var folder = process.argv[2]
var filter = require('./filtering')
var views = require('./views')

fs.readdir(folder, (err, files) => {
  if (err) throw err
  files.filter(file => { return path.extname(file) === '.txt' || path.extname(file) === '.md' }).forEach(file => {
    fs.readFile(path.join(folder, file), 'UTF-8', function(err, data) {
      if (err) throw err

      var parse_data = parse(data);
      var filter_data = filter.filter(parse_data, filter.tm);
      var vv = views(filter_data, []);
      vv.forEach(function (ll) {
        console.log(ll)
      })
      console.log('')
    })
  })
})


