function has_date(node, offsetStart, offsetEnd){
  if(node.date){
    var nodeDate = new Date(node.date);
    nodeDate = nodeDate.setHours(0, 0, 0, 0);

    offsetStart = offsetStart || 0;
    var startDate = new Date();
    startDate.setDate(startDate.getDate()+offsetStart)
    startDate = startDate.setHours(0, 0, 0, 0);

    if(!offsetEnd){
        console.log(nodeDate, startDate)
      return (nodeDate === startDate)
    } else {
      var endDate = new Date();
    endDate.setDate(endDate.getDate()+offsetEnd)
    endDate = endDate.setHours(0, 0, 0, 0);
      return ((nodeDate >= startDate) && (nodeDate <= endDate))
    }
  }
  return false;
}

function filter_td (node) {
  if (node.type === 'task') {
    return has_date(node)
  }
  return true
}

function filter_tm (node) {
    if (node.type === 'task') {
      return has_date(node, 1)
    }
    return true
}

function filter_wk (node) {
    if (node.type === 'task') {
      return has_date(node, 0,7)
    }
    return true
}

function filter_d (node) {
  if (node.type === 'task') {
    return (node.status==='done')
  }
  return true
}

//remove all empty nodes
function filter_prune(node){
    if(node.children){
        return (node.children.length>0)
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

function intersect(a,b){
    return function(node){
        return a(node) && b(node)
    }
}

function subtract(a,b){
    return function(node){
        return a(node) && !b(node)
    }
}

module.exports = {
  td: filter_td,
  tm: filter_tm,
  wk: filter_wk,
  d: filter_d,
  prune: filter_prune,

  union: union,
  intersect: intersect,
  subtract: subtract,

  filter: filter
}
