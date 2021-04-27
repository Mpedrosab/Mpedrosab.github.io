    var brd = JXG.JSXGraph.initBoard('jxgbox',{boundingbox:[-1,100,300,-10],axis:true});
var color = ['blue','orange', 'green','red','magenta', 'black','yellow'];
var nr = 0;
var maxX = 0.0;
var minX =  100000.0;
var maxY = 0.0;
var minY = 100000.0;
console.log("HEREEE")

//plotMyDB(myArrData['DPPC_B0420Y20']);
//plotMyDB(myArrData['Chol_B0414Y']); 


function splitData(myData){
    myData=myData.replace("[","").replace("]","")
    var splitArray=myData.split(",")
    splitArray=splitArray.map(Number);
   // console.log(splitArray);
    return splitArray;
}


function plotData(x,y) {
    var i;
    var x_arr = []; 
    var y_arr = [];
    var c
    var mycolor=nr%color.length;
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
        c=brd.create('point',[x[i],y[i]],{size:4,strokeWidth: 0,fillColor:color[mycolor]})
        
    }
    brd.setBoundingBox([-10,maxY+10,maxX+10,-10]);

    //Scatter plot
    //c = brd.create('curve', [x_arr, y_arr], {strokeWidth: 8,strokeColor:color[mycolor]})
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
 
function plotThisNames(){
        var value =document.getElementById("AllNamesSelect").value.split(", ");
    
    if ((Object.keys(value).length==1) && ((value[0] == null || value[0] == "" || value[0] == "any"))){
        console.log("No data selected");
    }
    else{
         for (const value2 of value){ 
             console.log(value2);
             //console.log(myArrData);
             plotMyDB(myArrData[value2]);
         }
    }
    eraseText("AllNamesSelect") 
}
   
          //document.getElementById("AllNames").addEventListener('click', function() { }, false);


//Add event listener
var notWorks=false;
document.querySelectorAll('.AllNamesSelect').forEach(item => {
    
    var key;
   
 if ( (item.attachEvent) && (notWorks==true)) {                  // For IE 8 and earlier versions
  item.attachEvent("onclick",function(){
      key=item.value;
    //console.log(item+" " +key)
      alreadyInput.push(key)
      alreadyInput.push(key)
      SetName(key,"AllNamesSelect");
      item.style.display = "none";
        //$('#'+key).hide()
});
     notWorks==true
}
      else if  ((item.addEventListener) && (notWorks==false)) {                    // For all major browsers, except IE 8 and earlier
  item.addEventListener("click",function(){
      key=item.value;
   // console.log(item+" " +key)
      
      SetName(key,"AllNamesSelect");
      item.style.display = "none";
        //$('#'+key).hide()
  });
        notWorks=false;
        
} 
});

var item;
/*********************
/*Plot button*/

item= document.getElementById("plot");
 if ( (item.attachEvent) && (notWorks==true)) {                  // For IE 8 and earlier versions
  item.attachEvent("onclick",function(){
plotThisNames()
      notWorks=true;
});
}
      else if  ((item.addEventListener) && (notWorks==false)){                    // For all major browsers, except IE 8 and earlier
  item.addEventListener("click",function(){
plotThisNames()
  });
        notWorks=false;
        
} 

/******************************/
/*Clear button*/


item= document.getElementById("ClearAll");
 if ( (item.attachEvent) && (notWorks==true)) {                  // For IE 8 and earlier versions
  item.attachEvent("onclick",function(){
   eraseText('AllNamesSelect');
    clearAll();
      
});
     notWorks==true
}
      else if ((item.addEventListener) && (notWorks==false)) {                    // For all major browsers, except IE 8 and earlier
  item.addEventListener("click",function(){
   eraseText('AllNamesSelect');
    clearAll();
  });
        notWorks=false;
        
} 


/************************************************/
/* Erase button */
item= document.getElementById("RemoveButton");
 if ( (item.attachEvent) && (notWorks==true)) {                  // For IE 8 and earlier versions
  item.attachEvent("onclick",function(){
   eraseText('AllNamesSelect');
for(var value of alreadyInput){
        console.log(value)
         document.getElementById(key).style.display = "block";
        
    }
    alreadyInput=[];
      
});
     notWorks==true
}
      else if ((item.addEventListener) && (notWorks==false)) {                    // For all major browsers, except IE 8 and earlier
  item.addEventListener("click",function(){
   eraseText('AllNamesSelect');
for(var value of alreadyInput){
        console.log(value)
         document.getElementById(key).style.display = "block";
        
    }
    alreadyInput=[];
  });
        notWorks=false;
        
} 


/*
for (var [key, value] of Object.entries(myArrData)){

    // onClick's logic below:
    //$('#AllNamesSelect').click( function() {
    console.log(key)
    document.getElementById(key).addEventListener('click', function(){
      SetName(key,"AllNamesSelect");
        $('#'+key).hide()
    })
    
}
*/




/*******************************************/
/* Insert selection*/
function SetName(location,output) {
      var txtName = document.getElementById(output);
    //console.log(document.getElementById(output).textContent)
      /*txtName.value = Array.prototype.filter.call( document.getElementById(location).textContent, el => el).map(el => el).join(",");*/
    var myID=document.getElementById(location).textContent;
    console.log(myID)
    if (txtName.value ==""){
        txtName.value =document.getElementById(myID).textContent;

    }
    else{
              txtName.value = txtName.value.concat(", "+document.getElementById(location).textContent);
        //console.log(document.getElementById(location).textContent);
    }

    };


/***********************************/
/* Clear text*/
function eraseText(myID) {
    document.getElementById(myID).value = "";

}
function clearAll(){
brd = JXG.JSXGraph.initBoard('jxgbox',{boundingbox:[-1,100,300,-10],axis:true});
   nr = 0;
maxX = 0.0;
minX =  100000.0;
maxY = 0.0;
minY = 100000.0;
    console.log(alreadyInput)
    for(var value of alreadyInput){
        console.log(value)
         document.getElementById(key).style.display = "block";
        
    }
    alreadyInput=[];
     //out=createFilter(myArrData,"AllNames");   //document.getElementById("AllNames").innerHTML=out;
}