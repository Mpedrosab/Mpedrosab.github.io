console.log("GraphFunctions")    
 console.log(filter)
var brd = JXG.JSXGraph.initBoard('jxgbox',{boundingbox:[-10,100,100,-10],axis:true});
var color = ['blue','orange', 'green','red','magenta', 'black','yellow'];
var nr = 0;
var maxX = 0.0;
var minX =  100000.0;
var maxY = 0.0;
var minY = 100000.0;






document.querySelectorAll('.dropSelect').forEach(item => {
 var key;
    item.addEventListener("click",function(){
      //console.log("Pro")
      key=item.id.replace("drop","Suggest");
    console.log(item+" " +key)
      var mySibling=document.getElementById(key)
    //console.log(mySibling.style.display)
if (mySibling.style.display == "block"){
    mySibling.style.display = "none"
}else{
    mySibling.style.display = "block"
}
//if (key!="NameSelect"){
//    $('.'+key).show()
//}
    });
    })


document.querySelectorAll('.SuggestedNameSelect').forEach(item => {

 var key;
           key=RestoreID(item.id);
    item.addEventListener("click",function(){
        
     // console.log("Pro")
  
      console.log(item+" " +key)

      SetName(key,"SuggestedNameSelect",true);
      item.style.display = "none"; 
//console.log(label) 
    });
    
    item.addEventListener("mouseover",function(){
        
        ShowDivSnapshot(key);
         document.getElementById("buttons_Plot").style.display="none";
        document.getElementById("snapShot-container").style.display="inline-block";
       
    })
     
      item.addEventListener("mouseleave",function(){
    
        
        document.getElementById("snapShot-container").style.display="none";
        document.getElementById("buttons_Plot").style.display="inline-block";
    })
    });  

addListenerToDropList("Substance1Suggest");
addListenerToDropList("TemperatureSuggest");
addListenerToDropList("SpeedSuggest");
//addListenerToDropLis(["Substance1Select"]);

function addListenerToDropList(label1){
 
       
 var label=label1.replace("Suggest","Select"); 
 var myParam=label1.replace("Suggest",""); 
       //console.log(label)
       document.querySelectorAll("."+label).forEach(item => {
 var key;
         
    item.addEventListener("click",function(){
       
      //console.log("Pro")
      key=RestoreID(item.id);
        var previousKey=String(document.getElementById(FixID(label)).value);
        var parent=document.querySelector('#'+label1);
        console.log('#\\'+previousKey+" ")
        if ((previousKey!="Any") &&(myParam=="Temperature")){
            previousKey='\\00003'+previousKey+" "
        }
         var child = parent ? parent.querySelector('#'+previousKey) : null;
        if (child!=null){
            child.style.display = "block"; 
        }
        else{
            console.log("PROBLEM WITH THOS ID!!")
        }
      
      SetName(key,String(label));
      item.style.display = "none"; 
        document.getElementById(FixID(label1)).style.display = "none";
console.log(key) 
        myArrOut=FilterNames(key,myParam,filter);
    });
    });  
     
}  
//??
//ARREGLAR QUERY SELECTOR CON DECIMALES!!!
//NO VUELVE A MOSTRAR LOS NOMBRES CON CLEARALL()!!
//QUE MUESTRE PLOT EN PEQUEÑO CON DATOS

/**************************************/
/*Plot data*/

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
        //c=brd.create('point',[x[i],y[i]],{size:4,strokeWidth: 0,fillColor:color[mycolor]})
        
    }
    brd.setBoundingBox([-10,maxY+10,maxX+10,-10]);

    //Scatter plot
    //c = brd.create('curve', [x_arr, y_arr], {strokeWidth: 8,strokeColor:color[mycolor]})
    brd.update();
    
    var d = brd.create('curve',[x,y],{strokeColor:color[nr%color.length],strokeWidth: 3});
    

    var A= brd.create('glider',[0, 0,d])
    	A.hideElement() 
    d.on('mouseover', function(e) {

   var myCords= getMouseCoords(e);
       
       // brd.create('point', [coords.usrCoords[1], coords.usrCoords[2]]);
        A = brd.create('glider',[myCords[0], myCords[1],d], {name:'['+myCords[2]+','+myCords[3]+']', strokeColor:"black",fillColor:'white'});
    //var point = brd.create('point', [0, 0], {withLabel: false, size: 1});
        if (d.mousemove){
        
            brd.removeObject(A);

        }
         
});  
    
    d.on('mousemove', function(e) {
  console.log("MOVED")
          A.hideElement();
   var myCords= getMouseCoords(e);
   A = brd.create('glider',[myCords[0], myCords[1],d], {name:'['+myCords[2]+','+myCords[3]+']', strokeColor:"black",fillColor:'white'});
     

       
}); 
     d.on('mouseout', function(e) {
  console.log("HERE PLOT")
              A.hideElement();
     

       
}); 

    nr++;
    brd.update();
};

function plotMyDB(dataToPlot){
    var x=splitData(dataToPlot["xData"]);
    var y=splitData(dataToPlot["yData"]);
    plotData(x,y);
};
 
function plotThisNames(){

        var value =document.getElementById("SuggestedNameSelect").value.split(", ");
    
    if ((Object.keys(value).length==1) && ((value[0] == null || value[0] == "" || value[0] == "any"))){
        alert("No data selected");
    }
    else{
         for (var value2 of value){ 
             //console.log(value2);
             //console.log(myArrData);
             plotMyDB(myArrData[value2]);
         }
    }
    eraseText("SuggestedNameSelect");
     document.getElementById("WaitToPlot").style.display = "none";
}
   
          //document.getElementById("AllNames").addEventListener('click', function() { }, false);


function getMouseCoords(e) {
    var i;
        var cPos = brd.getCoordsTopLeftCorner(e, i),
            absPos = JXG.getPosition(e, i),
            dx = absPos[0]-cPos[0],
            dy = absPos[1]-cPos[1];
   
        var obj=new JXG.Coords(JXG.COORDS_BY_SCREEN, [dx, dy], brd)
      
            var label=[Math.round((obj.usrCoords[1] + Number.EPSILON) * 100) / 100,Math.round((obj.usrCoords[2] + Number.EPSILON) * 100) / 100]
        return [obj.usrCoords[1], obj.usrCoords[2], label[0],label[1]];
    }


   

var item;
/*********************
/*Plot button*/


item= document.getElementById("plot");
item.onclick= function(){
     console.log( document.getElementById("WaitToPlot"))
     document.getElementById("WaitToPlot").style.display = "block";
setTimeout(() => {  plotThisNames(); }, 50);

}

document.getElementById("SuggestedNameRemove").addEventListener("click",function(){
    eraseText();
});
/******************************/
/*Filter Names*/


function FilterNames(key,paramFilter,filter){
        var myHTMLNow=document.querySelector('#NameSuggest');
    //No change from previous
    console.log(filter)
    if (filter[paramFilter] == key  ){
        return myArrNow;
    }
       //Add to global filter
    console.log("HEREE")
    console.log(filter)
var deletedKeys=[];
    if (filter[paramFilter] =="Any"){       //Previous was any, so dont have to filter again
            var filterOut=JSON.parse(JSON.stringify(myArrNow));
            filter[paramFilter] = key;
        console.log(filter)
        for (var TotalArrKey of Object.keys(filterOut).values()){ 
            if (deletedKeys.includes(TotalArrKey)){
                break;
            }
            if(filterOut[TotalArrKey][paramFilter]!=key){
                delete filterOut[TotalArrKey];
                deletedKeys.push(TotalArrKey);
             child = myHTMLNow ? myHTMLNow.querySelector('#'+myArr[TotalArrKey]["Name"]) : null; 
                     //UPDATE TO 1 JS!
                     
                     if (child!="null"){
                        document.querySelector('#'+myArr[TotalArrKey]["Name"]).style.display="none";
                         
                     }
                     else{
                         console.log("NO CHILD FOUND")
                     }   
        }
    }
    
    

}
    
   // var child;
   // filterStartDate=parseDate(filterStartDate);
   // filterEndDate=parseDate(filterEndDate);
 
   else{
        console.log("ISNOTANY")
       filter[paramFilter] = key;
       var filterOut=JSON.parse(JSON.stringify(myArr))
       for (var TotalArrKey of Object.keys(myArr).values()){    //Restore all values and then filter

           child = myHTMLNow ? myHTMLNow.querySelector('#'+myArr[TotalArrKey]["Name"]) : null;
              if(child==null){
                         console.log("NO CHILD FOUND") 
             }
             else{
                 
                 console.log("restore")
                 console.log(child.style.display)
                   document.querySelector('#'+myArr[TotalArrKey]["Name"]).style.display="block";
                 console.log(child.style.display)
             }
       }
       for (var TotalArrKey of Object.keys(myArr).values()){ 
                  if (deletedKeys.includes(TotalArrKey)){
                break;
        }
         for (const [paramFilter2, value] of Object.entries(filter)) {
             child = myHTMLNow ? myHTMLNow.querySelector('#'+myArr[TotalArrKey]["Name"]) : null;
              if(child==null){
                         console.log("NO CHILD FOUND")
             }
             else{
             if (value == "Any"){
             
                console.log("noFilter "+paramFilter2)
        }
             else{
                 if(filterOut[TotalArrKey][paramFilter2]!=value){
                                        
                     //UPDATE TO 1 JS!
                document.querySelector('#'+myArr[TotalArrKey]["Name"]).style.display="none";
                     console.log("Removed:")  
                     console.log(document.querySelector('#'+myArr[TotalArrKey]["Name"])) 
                     delete filterOut[TotalArrKey]; 
                     deletedKeys.push(TotalArrKey);
                 }
                 else{
                      console.log("Saved:") 
                      console.log(document.querySelector('#'+myArr[TotalArrKey]["Name"])) 
                 }

             }
         }
         }
    }
    
    }
console.log(filterOut)
    return filterOut;
}



/*******************************************/
/* Insert selection*/
function SetName(location,output,fromName=false) {
    var textOut=document.getElementById(FixID(location)).textContent;
     var txtName = document.getElementById(FixID(output));
if (fromName!=true){
         
    txtName.value =textOut;
    }
    else{

     
    console.log(output)
    console.log(txtName.value)

    if (txtName.value ==""){
        txtName.value =textOut;

    }
    else{
              txtName.value = txtName.value.concat(", "+textOut);
        //console.log(document.getElementById(location).textContent);
    }

    }};

/***********************************/
document.getElementById("ClearPlot").addEventListener("click",function(){
     clearPlot();
});  
/* Clear text*/
function eraseText() {
       document.getElementById("SuggestedNameSelect").value="";
document.querySelectorAll('.SuggestedNameSelect').forEach(item => {item.style.display == "block"});
}
         
 document.getElementById("ClearAll").addEventListener("click",function(){
     clearAll();
});  

      

function clearAll(){
    document.querySelectorAll('.Substance1Select').forEach(item => {item.style.display = "block"});
document.querySelectorAll('.TemperatureSelect').forEach(item => {item.style.display = "block"});
document.querySelectorAll('.SpeedSelect').forEach(item => {item.style.display = "block"});
document.querySelectorAll('.SuggestedNameSelect').forEach(item => {item.style.display = "block"; console.log("HEREEE")});
    
            document.getElementById("SuggestedNameSelect").value="";
    document.getElementById("Substance1Select").value="Any";
    document.getElementById("SpeedSelect").value="Any";
    document.getElementById("TemperatureSelect").value="Any";
    document.getElementById("startDate").value=null;
    document.getElementById("endDate").value=null;
    

        

    alreadyInput=[];
    
}
         
function clearPlot(){
brd = JXG.JSXGraph.initBoard('jxgbox',{boundingbox:[-10,100,100,-10],axis:true});
   nr = 0;
maxX = 0.0;
minX =  100000.0;
maxY = 0.0;
minY = 100000.0;



//if (key!="NameSelect"){
//    $('.'+key).show()
//}

clearAll();
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