

/*Load Json at start*/

var myArrData=[];
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
  var myArrDataPrev = JSON.parse(this.responseText); 
  //myArrData = JSON.stringify(myArrData);
  //myArrData = jQuery.parseJSON(myArrData);
      arrayDataLength = Object.keys(myArrDataPrev).length;
    
      console.log(myArrData);
      myArrNow=JSON.parse(JSON.stringify(myArr));       //Copy array is being 
        arrayNowDataLength = Object.keys(myArrNow).length;
      dataLoaded=true; 
        console.log(Object.keys(myArrDataPrev));
      
      //Sort by date
      for(var [key, value] of Object.entries(myArr)){
myArrData[value["Name"]]=[]
          //console.log(myArrDataPrev[value["Name"]]);
          //console.log(value["Name"]);
          myArrData[value["Name"]]["xData"]=myArrDataPrev[value["Name"]]["xData"]
          myArrData[value["Name"]]["yData"]=myArrDataPrev[value["Name"]]["yData"]
          myArrData[value["Name"]]["yParam"]=myArrDataPrev[value["Name"]]["yParam"]
          myArrData[value["Name"]]["xParam"]=myArrDataPrev[value["Name"]]["xParam"]
      }
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
      
      var divSnapshot=createDivSnapshot(myArr);
     document.getElementById("snapShot-container").innerHTML=divSnapshot;
      document.getElementById("snapShot-container").style.display="none";
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


/*****************************************************************/
/*Create snapShot with data*/
 function createDivSnapshot(arr){
        var str='<div class="snapShot" id="myName_snapShot">\
            <a href="/myHTML" class="">\
            <img src="/myIMG" class="button snapShot-img"><div class="snapShot-data button"><span class="substance">mySubstance:</span><span> T= myTemp °C</span><br><span>V= myVol myVolUnit [myConc myUnitConc]</span><br><span>speed= mySpeed myUnitSpeed </span><br><span>Date: myDate</span></div>\
       </a> </div>\
          '
     var strOut="<p class='snapShot-preview'>Preview:</p>";
      for (const [key, value] of Object.entries(arr)){
                      
          strOut+=str.replace("myIMG",value["IMG"]).replace("myName",FixID(value["Name"])).replace("myHTML",value["HTML"]).replace("mySubstance",value["Substance1"]).replace("mySubstance",value["Substance1"]).replace("myVol",value["Volume1"]).replace("myVolUnit",value["Unit_Vol"]).replace("myUnitConc",value["Unit1"]).replace("myConc",value["Concentration1"]).replace("myTemp",value["Temperature"]).replace("mySpeed",value["Speed"]).replace("myDate",value["Date"].split(" ")[0]).replace("myUnitSpeed",value["Unit_Speed"])  //Remove date time from date
          
      }
     console.log("createDiv")
     //console.log(strOut)
     return strOut;
     
 };


/******************************************/
function ShowDivSnapshot(key){
    document.querySelectorAll(".snapShot").forEach(item=>{
        
        item.style.display="none";
        
    })
   console.log(key+"snapShot");
    document.getElementById(FixID(key)+"_snapShot").style.display="block"
    
}