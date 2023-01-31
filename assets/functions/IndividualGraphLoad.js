

/*Load Json at start*/

var myArrData=[];
var myArrNow;
var arrayDataLength;
var arrayNowDataLength;
var dataLoaded;
var filter=[];
var x;
var y;
var distZero= []; //Stores the distance to the origin to find where is the mouse
var distZeroManhattan= []; //Stores the distance to the origin to find where is the mouse
var minDist=0; //Minimum difference between distances
var img;
var imgArray = [];  //Stores not nan values
var value;
var maxX = 0.0;
var minX =  100000.0;
var maxY = 0.0;
var minY = 100000.0;
var colorLegend=[];
var labelLegend=[];
var labelLegend=[];

console.log("IndividualGraphLoad")
 $(document).ready(function(){ 
var xmlhttpData = new XMLHttpRequest(); 
xmlhttpData.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
      //console.log("Good");  
  var myArrData = JSON.parse(this.responseText); 
  //myArrData = JSON.stringify(myArrData);
  //myArrData = jQuery.parseJSON(myArrData);
      arrayDataLength = Object.keys(myArrData).length;
    
      //console.log(myArrData);
      myArrNow=JSON.parse(JSON.stringify(myArr));       //Copy array is being 
        arrayNowDataLength = Object.keys(myArrNow).length;
      dataLoaded=true; 
        //console.log(Object.keys(myArrData));

      //Get the data to plot


 value =document.getElementById("myIsothermPlot").innerHTML;
value=value.trim();
 x=splitData(myArrData[value]["xData"]);
 y=splitData(myArrData[value]["yData"]);

      xparam= myArrData[value]["xParam"]
      yparam=myArrData[value]["yParam"]
       x=splitArray=x.map(Number);
       var yOld=splitArray=y.map(Number);
img=splitData(myArrData[value]["BAMimg"]);

      //Find distance to origin
      //distZero=Math.sqrt(Math.abs(x)*Math.abs(x)+Math.abs(y)*Math.abs(y))
    var i;
    var x_arr = []; 
    var y_arr = [];
    var y0=y[0];
      y = yOld.map(function(e) { 
  return e-y0;
}); 
 //imgArray = noFind("nan",img);
 //console.log(imgArray);
      maxX=Math.max.apply(null,x);
      minX=Math.min.apply(null,x);
      minX=Math.min.apply(null,y);
      maxY=Math.max.apply(null,y);
      
      
    for (i=0;i<x.length-1;i++) {
        
       // distZero[i]=Math.sqrt((x[i]*x[i]+y[i]*y[i]))
    //    distZeroManhattan[i]=Math.abs(x[i])+Math.abs(y[i])
        

        //Remove bias

        //y[i]=y[i]-y0;
        //if (x[i]>maxX) maxX = x[i];
        //if (x[i]<minX) minX = x[i];
        //if (y[i]>maxY) maxY = y[i];
        ////if (y[i]<minY) minY = y[i];
        if (img[i]!="nan"){ imgArray.push(i); }
        //x_arr.push(x[i], x[i], NaN);
        //y_arr.push(y[i], y[i], NaN);
        //c=brd.create('point',[x[i],y[i]],{size:4,strokeWidth: 0,fillColor:color[mycolor]})
        
    }
    
       
        //var out=createFilter(myArrData,"AllNames");    

    document.getElementById("Slider").innerHTML='  <input id="sliderVal" type="range" min="0" max="'+String(x.length-1)+'" value="0" onchange="movePoint()" oninput="movePoint()" >';
    //console.log("LoadGraphFunctions")
    $.getScript("/assets/functions/IndividualGraphFunctions.js");
    $.getScript("https://code.jquery.com/jquery-3.2.1.min.js");
    
      
  }
    else{
        //console.log ("Problem with JSON for data file!! =>Stataus: " +this.status );
        dataLoaded=false;
    }
};
xmlhttpData.open("GET", "/Data/DataDB.json", true);
xmlhttpData.send(); 
    
})


function splitData(myData){
    myData=myData.replace("[","").replace("]","")
    var splitArray=myData.split(",")
   
   // //console.log(splitArray);
    return splitArray;
}

function noFind(needle, haystack) {
    needle=String(needle)
    //console.log(needle);
    var results = [];
    for (i=0;i<haystack.length-1;i++){
if (haystack[i]!=needle){ results.push(i); }
    return results;
        }
}
