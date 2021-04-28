    var brd = JXG.JSXGraph.initBoard('jxgbox',{boundingbox:[-1,100,300,-10],axis:true});
var color = ['blue','orange', 'green','red','magenta', 'black','yellow'];
var nr = 0;
var maxX = 0.0;
var minX =  100000.0;
var maxY = 0.0;
var minY = 100000.0;

var myList=document.getElementById("collapsible");
//plotMyDB(myArrData['DPPC_B0420Y20']);
//plotMyDB(myArrData['Chol_B0414Y']); 
 document.getElementById("WaitToPlot").style.display = "none";
myList.addEventListener("click",function(){
    var mySibling=myList.querySelector("#AllNamesList")
    //console.log(mySibling.style.display)
if (mySibling.style.display == "block"){
    mySibling.style.display = "none"
}else{
    mySibling.style.display = "block"
}
});

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
        alert("No data selected");
    }
    else{
         for (const value2 of value){ 
             //console.log(value2);
             //console.log(myArrData);
             plotMyDB(myArrData[value2]);
         }
    }
    eraseText("AllNamesSelect");
     document.getElementById("WaitToPlot").style.display = "none";
}
   
          //document.getElementById("AllNames").addEventListener('click', function() { }, false);

//Add event listener
var notWorks=true;
document.querySelectorAll('.AllNamesSelect').forEach(item => {
 var key;
    item.addEventListener("click",function(){
      //console.log("Pro")
      key=item.id;
   // console.log(item+" " +key)
      
      SetName(key,"AllNamesSelect");
      item.style.display = "none";
    });
    });
   

var item;
/*********************
/*Plot button*/

/*
 if ( (item.attachEvent)) {                  // For IE 8 and earlier versions
      console.log("Basic")
  item.attachEvent("onclick",function(){
plotThisNames()
      notWorks=true;
});
}s
      else if  ((item.addEventListener) ){   
           console.log("Basic")// For all major browsers, except IE 8 and earlier
  item.addEventListener("click",function(){
plotThisNames()
  });
        notWorks=false;
        

}
} 
*/
item= document.getElementById("plot");
item.onclick= function(){
     console.log( document.getElementById("WaitToPlot"))
     document.getElementById("WaitToPlot").style.display = "block";
setTimeout(() => {  plotThisNames(); }, 500);

}
/******************************/
/*Clear button*/


item= document.getElementById("ClearAll");

  item.addEventListener("click",function(){
   eraseText('AllNamesSelect');
    clearAll();
  });



/************************************************/
/* Erase button */
    item= document.getElementById("RemoveSelect");
     item.addEventListener("click",function(){
   eraseText('AllNamesSelect');
for(var value of alreadyInput){
        console.log(value)
         document.getElementById(key).style.display = "block";
        
    }
    alreadyInput=[];
      });
    /*
item= document.getElementById("RemoveButton");
 if ( (item.attachEvent)) {                  // For IE 8 and earlier versions
     
  item.attachEvent("onclick",function(){
   eraseText('AllNamesSelect');
for(var value of alreadyInput){
        console.log(value)
         document.getElementById(key).style.display = "block";
        
    }
    alreadyInput=[];
      
});
     notWorks=true
}
      else if ((item.addEventListener)) {                    // For all major browsers, except IE 8 and earlier
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
*/






/*******************************************/
/* Insert selection*/
function SetName(location,output) {
      var txtName = document.getElementById(output);
    //console.log(document.getElementById(output).textContent)
      /*txtName.value = Array.prototype.filter.call( document.getElementById(location).textContent, el => el).map(el => el).join(",");*/
    console.log(location)
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

    for(var value of alreadyInput){
        console.log(value)
         document.getElementById(value).style.display = "block";
        
    }
    alreadyInput=[];
     //out=createFilter(myArrData,"AllNames");   //document.getElementById("AllNames").innerHTML=out;
}
/*
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
*/