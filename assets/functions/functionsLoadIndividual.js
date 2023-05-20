
/*Load Json at start*/
var myArr;
var arrayLength;
var alreadyInput=[];

/*****************************************/
window.onload = function () {
var xmlhttp = new XMLHttpRequest();
//fetch( "/borrar.json").then(response => response.json()) 

//console.log(response)
    xmlhttp.open("GET", "/Data/ParamDB.json", true);
    
xmlhttp.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
      console.log("Good");
    
  myArr = jQuery.parseJSON(this.responseText);
      arrayLength = Object.keys(myArr).length;
   // console.log(myArr);
 
          $(document).ready(function(){ 
              document.getElementById("BAMimg").innerHTML='<h2 style="display:block; width: 300%; margin-left:300% !important">Loading ...</h2>'
           
                  $.getScript("/assets/functions/IndividualGraphLoad.js");
              
      console.log("HOLA")
         //Create Div


       
      });
  }
    else{
        console.log ("Problem with JSON file!! =>Stataus: " +this.status );
        
    }
};


xmlhttp.send(); 

    
};

/**************************************************/
/*Create filter for header page*/
    function createFilter(arr,parameter){
    var str="";
    
   // var allFunct="SetName( 'location','Select'); $('#location').hide()"
    //var functions='onclick="myFunction">';                                                  
    for (var [key, value] of Object.entries(arr))
{
    if (alreadyInput.includes(value[parameter])==false){
 // str += "<option id='"+key+"' value='"+key+"' class='Select' "+functions+key+"</option>";
  str += "<li id='"+FixID(value[parameter])+"'  class='Select' style='display:block'>"+value[parameter]+"</li>";
        alreadyInput.push(value[parameter])
        //str=str.replaceAll("myFunction",allFunct).replaceAll("location",key);
       // str=str.replaceAll("location",value[parameter]);
  } 
}
   str= str.replaceAll('myParam',parameter).replaceAll("Select",parameter+"Select");

    return str;
};



/*****************************************************************/
/*Create div with data*/
 function createDiv(arr){
        var str='<div class="overlay">\
            <img src="/myIMG""><div class="button"><a href="/myHTML" class="button"><h2 class="button">mySubstance</h2><br>Date: myDate<br>V= myVol myVolUnit [myConc myUnitConc]<br>T= myTemp °C; speed= mySpeed myUnitSpeed</a></div>\
        </div>\
          '
     var strOut="";
      for (const [key, value] of Object.entries(arr)){
                      
         value["Substance1"]=value["Substance1"].replace(":Cur=","+Cur<br>χ=")
         if (value["Substance1"].includes("<br>")){
             str=str.replace("<br>Date:","Date:")
         }
          strOut+=str.replace("myIMG",value["IMG"]).replace("myHTML",value["HTML"]).replace("mySubstance",value["Substance1"]).replace("mySubstance",value["Substance1"]).replace("myVol",value["Volume1"]).replace("myVolUnit",value["Unit_Vol"]).replace("myUnitConc",value["Unit1"]).replace("myConc",value["Concentration1"]).replace("myTemp",value["Temperature"]).replace("mySpeed",value["Speed"]).replace("myDate",value["Date"].split(" ")[0]).replace("myUnitSpeed",value["Unit_Speed"])  //Remove date time from date
          
      }
     console.log("createDiv")
     //console.log(strOut)
     return strOut;
     
 };


/**************************************************/
/*Order by date*/
function sortByDate(arr){
    var sortable = [];
    var arrOut = {};

for (var [key, value] of Object.entries(arr)){
    sortable.push([key, value["Date"]]);
}
sortable.sort(function(a, b) {
    return -(new parseDate(a[1]) - new parseDate(b[1]));
});
    //Relace initial array
    var i=0;
        for (const value of sortable) {
            arrOut[i]=arr[value[0]];
            i+=1;
}   
    return arrOut;
      
};


/******************************************************/
/*String to date*/
function parseDate(s) {
  var b = s.split(" ")[0];
  b = b.split(/\D/);
    //console.log(b)
    //console.log(new Date(b[0], --b[1], b[2]))
  return new Date(b[0], --b[1], b[2]);
}


/*******************************************************/
/* Fix numbers for ID  */

function FixID(value){
    value=String(value)
    var firstChar = value.charAt(0);
if( firstChar <='9' && firstChar >='0') {
      value="number-"+value;
}
    value=value.replace(".","_");
    return value;
    
}
function RestoreID(value){
    if (value.indexOf("number-")>=0){
            value=value.replace("number-","");
     value=value.replace("_","."); 
    }
    return value
}
