function sub(){
  product = document.getElementsByID("prod")[0].value;
  shelf = document.getElementsByID("shelf")[0].value;
    var mysql = require('mysql');

var con = mysql.createConnection({
  host: "ParamDB.db",

});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});

};