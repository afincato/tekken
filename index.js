var fs = require('fs');
var date_rx = /\sd\((\d\d)-(\d\d)-(\d\d\d\d)\)/

function parse_line (line) {
  var section = line.substring(0, 2);
  if (section === '##') {
    return {
      type: 'header',
      value: line.substring(3)
    }
  }

  var task = line.match(/- \[(.)\]\s/)
  if (task) {
    return {
      type: 'task',
      value: line.substring(6).replace(date_rx, ''),
      date: parse_date(line.substring(6)),
      status: parse_status(task[1])
    }
  }
}

function parse_date (value) {
  var date = value.match(date_rx);
  if (date) {
    date = new Date (date[3], date[2], date[1])
  }
  console.log(date)
  return date
}

function parse_status (value) {
  var status = {
    'x' : 'done',
    ' ' : 'not done',
    'w' : 'waiting',
    'c' : 'cancelled',
  }
  return status[value]
}

fs.readFile('waa.todo.txt', 'UTF-8', function(err, data) {
  var lines = data.split('\n')

  lines = lines.map(parse_line).filter(function(line){
    return line
  })

  console.log(lines);
})


