function filter_td (node) {
  if (node.type === 'task') {
    var today = new Date();
    return (node.date && today.setHours(0, 0, 0, 0) === node.date.setHours(0, 0, 0, 0))
  }
  return true
}

function filter_tm (node) {
  if (node.type === 'task') {
    var tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate()+1);
    return (node.date && tomorrow.setHours(0, 0, 0, 0) === node.date.setHours(0, 0, 0, 0))
  }
  return true
}

function filter_d (node) {
  if (node.type === 'task') {
    return (node.status==='done')
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

//composition
function union(a,b){
    return function(node){
        return a(node) || b(node)
    }
}

function overlap(a,b){
    return function(node){
        return a(node) && b(node)
    }
}

module.exports = {
  td: filter_td,
  tm: filter_tm,
  d: filter_d,
  union: union,
  overlap: overlap,
  filter: filter
}
