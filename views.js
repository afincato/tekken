var conv = require("./conversion")

function input (node) {
  if (node.type === 'header') {
    return new Array(node.level +1).join('#') + ' ' + node.value
  }

  if (node.type === 'task') {
    var date = "";
    if(node.date){
        date = conv.write_date(node.date)
    }

    return '- [' + conv.write_status(node.status) + '] ' + node.value + date
  }
}

function walk_node (node, lines) {
  var ii = input(node)
  if (ii) {
    lines.push(ii)
  }

  if (node.children) {
    node.children.forEach(function (child){
      walk_node(child, lines)
    })
  }
  return lines

}

module.exports = walk_node
