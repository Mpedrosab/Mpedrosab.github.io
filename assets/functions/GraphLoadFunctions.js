

/*Load Json at start*/

var myArrData;
var myArrNow;
var arrayDataLength;
var arrayNowDataLength;
var dataLoaded;
var filter=[];

console.log("GraphLoad")
 $(document).ready(function(){ 
var xmlhttpData = new XMLHttpRequest();
xmlhttpData.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
      console.log("Good");  
  myArrData = JSON.parse(this.responseText); 
  //myArrData = JSON.stringify(myArrData);
  //myArrData = jQuery.parseJSON(myArrData);
      arrayDataLength = Object.keys(myArrData).length;
    
      console.log(myArrData);
      myArrNow=JSON.parse(JSON.stringify(myArr));       //Copy array is being 
        arrayNowDataLength = Object.keys(myArrNow).length;
      dataLoaded=true; 
        console.log(Object.keys(myArrData));
        //var out=createFilter(myArrData,"AllNames");   
     //    document.getElementById("AllNamesList").style.display = "none"
     // document.getElementById("AllNamesList").innerHTML=out;

      
      //var myEl = $('.Chol_B0423Xss');
document.getElementById("Substance1Suggest").innerHTML=document.getElementById("Substance1Suggest").innerHTML+ "<li id='Any'  class='Substance1Select' style='display:block'>Any</li>";  

      document.getElementById("TemperatureSuggest").innerHTML=document.getElementById("TemperatureSuggest").innerHTML+ "<li id='Any'  class='TemperatureSelect' style='display:block'>Any</li>";   document.getElementById("SpeedSuggest").innerHTML=document.getElementById("SpeedSuggest").innerHTML+ "<li id='Any'  class='SpeedSelect' style='display:none'>Any</li>";   
   filter["Substance1"]="Any";
   filter["Temperature"]="Any";
   filter["Speed"]="Any";
document.getElementById("TemperatureSelect").value="Any";
document.getElementById("Substance1Select").value="Any";
document.getElementById("SpeedSelect").value="Any";
      console.log(filter)
      document.getElementById("WaitToPlot").style.display = "none"

    console.log("LoadGraphFunctions")
    $.getScript("/assets/functions/GraphFunctions.js");
    $.getScript("https://code.jquery.com/jquery-3.2.1.min.js");


 

  }
    else{
        console.log ("Problem with JSON for data file!! =>Stataus: " +this.status );
        dataLoaded=false;
    }
};
xmlhttpData.open("GET", "/Data/DataDB.json", true);
xmlhttpData.send(); 
    
})

 