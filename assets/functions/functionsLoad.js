
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
     var myURL= window.location.href;
  myArr = jQuery.parseJSON(this.responseText);
      arrayLength = Object.keys(myArr).length;
     // console.log(JSON.stringify(myArr));
      //Order by date
          myArr=sortByDate(myArr);
   // console.log(myArr);
    //Create  selections
    var out=createFilter(myArr,"Substance1");   
    document.getElementById("Substance1Suggest").innerHTML=out;
    out=createFilter(myArr,"Temperature");     
    document.getElementById("TemperatureSuggest").innerHTML=out;
    out=createFilter(myArr,"Speed");     
       
       document.getElementById("SpeedSuggest").innerHTML=out;



      
      
     out= CreateSuggest(myArr,"Name")
     document.getElementById("NameSuggest").innerHTML=out;
     
          $(document).ready(function(){ 

      console.log("HOLA")
         //Create Div
              
      if (myURL.indexOf("comparison")<0){
       out=createDiv(myArr);
      //console.log(out);
      document.getElementById("isotherm_button_in").innerHTML=out;
          
     
    $.getScript("https://code.jquery.com/jquery-3.2.1.min.js");
    $.getScript("/assets/functions/functions.js");

     }
       document.getElementById("NameSuggest").style.display = "none"
       document.getElementById("Substance1Suggest").style.display = "none"
       document.getElementById("TemperatureSuggest").style.display = "none"
       document.getElementById("SpeedSuggest").style.display = "none"
       
      });
  }
    else{
        console.log ("Problem with JSON file!! =>Stataus: " +this.status );
        
    }
};


xmlhttp.send(); 
    
     document.getElementById('NameSuggest').style.display = "none"; //Hide name suggestins
    

    
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
  str += "<li id='"+value[parameter]+"'  class='Select' style='display:block'>"+value[parameter]+"</li>";
        alreadyInput.push(value[parameter])
        //str=str.replaceAll("myFunction",allFunct).replaceAll("location",key);
        str=str.replaceAll("location",value[parameter]);
  } 
}
   str= str.replaceAll('myParam',parameter).replaceAll("Select",parameter+"Select");

    return str;
};



/*****************************************************************/
/*Create div with data*/
 function createDiv(arr){
        var str='<div class="overlay">\
            <img src="/myIMG" class="button"><div class="button"><a href="/myHTML" class="button"><h2 class="button">mySubstance</h2><br>Date: myDate<br>V= myVol myVolUnit [myConc myUnitConc]<br>T= myTemp °C; speed= mySpeed myUnitSpeed</a></div>\
        </div>\
          '
     var strOut="";
      for (const [key, value] of Object.entries(arr)){
                      
          strOut+=str.replace("myIMG",value["IMG"]).replace("myHTML",value["HTML"]).replace("mySubstance",value["Substance1"]).replace("mySubstance",value["Substance1"]).replace("myVol",value["Volume1"]).replace("myVolUnit",value["Unit_Vol"]).replace("myUnitConc",value["Unit1"]).replace("myConc",value["Concentration1"]).replace("myTemp",value["Temperature"]).replace("mySpeed",value["Speed"]).replace("myDate",value["Date"].split(" ")[0]).replace("myUnitSpeed",value["Unit_Speed"])  //Remove date time from date
          
      }
     console.log("createDiv")
     //console.log(strOut)
     return strOut;
     
 };

/**************************************/
/*Create list of suggestions*/
function CreateSuggest(array,parameter){
    //Parameter => what parameter to compare
var srt = "";
    var tempstr;
    
for (var [key, value] of Object.entries(array))
{
        //console.log("HERE")
           tempstr= "<li class='SuggestedNameSelect' id='myVal' style='display:block' >myVal</li>";
        tempstr=tempstr.replaceAll("myVal",value[parameter])
        srt +=tempstr;  
 
    }
 
         srt += "<li id='noMatchesName' style='display:none'>No matches found!!</li>";
     

return srt;
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
