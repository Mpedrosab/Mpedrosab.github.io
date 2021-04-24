

function sub(){
    var name = document.getElementById("name").value;
    var start = document.getElementById("start").value;
    var end = document.getElementById("end").value;
    var dppc = document.getElementById("cDPPC").checked;
    var chol = document.getElementById("cChol").checked;
        if (end==""){
        end="-"
    }
     alert (name+start+end+dppc+chol);
var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    document.getElementById("demo").innerHTML = this.responseText;
  }
        };
    xmlhttp.open("GET", "functions.php?HEY=hey", true);
xmlhttp.send();
    
};
    
function createQuery(){
    
    
};
   





