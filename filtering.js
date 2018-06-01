function filter_td (node) {
  if (node.type === 'task') {
    var today = new Date();
    if (node.date && today.setHours(0, 0, 0, 0) === node.date.setHours(0, 0, 0, 0)) {
      return true
    } else {
      return false
    }
  } 
  return true
}

function filter_tm (node) {
  if (node.type === 'task') {
    var tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate()+1);
    if (node.date && tomorrow.setHours(0, 0, 0, 0) === node.date.setHours(0, 0, 0, 0)) {
      return true
    } else {
      return false
    }
  } 
  return true
}

function filter(node, callback){
  if (node.children) {
    node.children = node.children.map(function (child){
      return filter(child, callback)
    }).filter(function (child) {
      return child
    })
  }

  var t = callback(node)
  if (t) return node
  return undefined
}

module.exports = {
  td: filter_td,
  tm: filter_tm,
  filter: filter
}
