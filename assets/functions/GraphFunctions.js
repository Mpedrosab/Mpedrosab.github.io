

/*Load Json at start*/
var myArr;
var arrayLength;
var myArrData;
var arrayDataLength;


window.onload = function () {
var xmlhttpData = new XMLHttpRequest();
xmlhttpData.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
      console.log("Good");
  myArrData = JSON.parse(this.responseText);
  //myArrData = JSON.stringify(myArrData);
  //myArrData = jQuery.parseJSON(myArrData);
      arrayDataLength = Object.keys(myArrData).length;
      console.log(myArrData);
    console.log(Object.keys(myArrData));
plotMyDB(myArrData['DPPC_B0420Y20']);
plotMyDB(myArrData['Chol_B0414Y']);

  }
    else{
        console.log ("Problem with JSON for data file!! =>Stataus: " +this.status );
        
    }
};
xmlhttpData.open("GET", "/Data/DataDB.json", true);
xmlhttpData.send(); 


};



    var brd = JXG.JSXGraph.initBoard('jxgbox',{boundingbox:[-1,100,300,-10],axis:true});
var color = ['blue','orange', 'green','red','magenta', 'black','yellow'];
var nr = 0;
var maxX = 0.0;
var minX =  100000.0;
var maxY = 0.0;
var minY = 100000.0;
    
    



function splitData(myData){
    myData=myData.replace("[","").replace("]","")
    var splitArray=myData.split(",")
    splitArray=splitArray.map(Number);
    console.log(splitArray);
    return splitArray;
}


function plotData(x,y) {
    var i;
    var x_arr = []; 
    var y_arr = [];
    //var t = document.getElementById('jxgbox').value;
   // var data = t.split('\n');
    var y0=y[0];
    for (i=0;i<x.length-1;i++) {
        
        
        //Remove bias

        y[i]=y[i]-y0;
        if (x[i]>maxX) maxX = x[i];
        if (x[i]<minX) minX = x[i];
        if (y[i]>maxY) maxY = y[i];
        if (y[i]<minY) minY = y[i];
        x_arr.push(x[i], x[i], NaN);
        y_arr.push(y[i], y[i], NaN);
        
        
    }
    brd.setBoundingBox([-10,maxY+10,maxX+10,-10]);

    //Scatter plot
    var c = brd.create('curve', [x_arr, y_arr], {strokeWidth: 8,strokeColor:color[nr%color.length]})
    brd.update();
    
    var d = brd.create('curve',[x,y],{strokeColor:color[nr%color.length],strokeWidth: 3});
    nr++;
    brd.update();
};

function plotMyDB(dataToPlot){
    var x=splitData(dataToPlot["xData"]);
    var y=splitData(dataToPlot["yData"]);
    plotData(x,y);
};


