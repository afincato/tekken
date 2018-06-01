var date_rx = /\sd\((\d\d)-(\d\d)-(\d\d\d\d)\)/

function parse (data) {
  var lines = data.split('\n')

  lines = lines.map(parse_line).filter(function(line){
    return line
  })

  return parse_tree(lines);
}

function parse_line (line) {
  var section = line.match(/#+\s/);

  if (section) {
    return {
      type: 'header',
      value: line.substring(section[0].length),
      level: section[0].length -1
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
    date = new Date (date[3] + "-" + date[2] + "-" + date[1])
  }
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

function parse_tree (lines, level) {
  var stack = [{level: 0}]
  var tree = {type: 'root', children: []}
  var leaf = tree

  lines.forEach(function(line) {

    if (line.type === 'header') {
      line.children = []

      // if the levels are the same: replace top of stack
      if (line.level === stack[stack.length -1].level) {
        stack.pop()
        leaf = stack[stack.length -1]
        leaf.children.push(line)
        stack.push(line)
      // if the level is higher than the previous
      } else if (line.level > stack[stack.length -1].level) {
        stack.push(line)
        leaf.children.push(line)
      // if the level is lower than the previous
      } else {
        stack.pop()
        leaf.children.push(line)
      }

      leaf = stack[stack.length -1]
    }

    if (line.type === 'task') {
      leaf.children.push(line)
    }

  })

  return tree
}

module.exports = parse
