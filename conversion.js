var status = {
  'x': 'done' ,
  ' ': 'not done',
  'w': 'waiting' ,
  'c': 'cancelled' ,
}

function read_status(s){
  return status[s]
}

function write_status(s){
  for( var prop in status ) {
    if( status.hasOwnProperty( prop ) ) {
      if( status[ prop ] === s )
        return prop;
      }
    }
}

//convert from string to date
function read_date(date){
  return new Date (date[3] + "-" + date[2] + "-" + date[1])
}

//convert from date object to string
function write_date(inputdate){
  function pad(s) { return (s < 10) ? '0' + s : s; }
  var d = new Date(inputdate)
  var date = [pad(d.getDate()), pad(d.getMonth()+1), d.getFullYear()].join('-')
  return "d("+date+")"
}

module.exports = {
    read_status: read_status,
    write_status: write_status,
    read_date: read_date,
    write_date: write_date,
}
