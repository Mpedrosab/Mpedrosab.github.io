console.log("IndividualGraphFunctions")    
var xrange=x[0]-x[1]
var brd = JXG.JSXGraph.initBoard('jxgbox',{boundingbox:[-100*xrange,100,x[0]+xrange,-10],keepaspectratio:false ,axis:true,
      defaultAxes: {
    x : {
    name: xparam,
    withLabel: true,
    label: {
        position: 'rt',
      offset: [-100, -27]
    }
  },
  y : {
    withLabel:true,
    name: yparam,
      label: {
        position: 'rt',
           offset: [10, 0]
        
      }
    }}});

var color = ['blue','orange', 'green','red','magenta', 'black','yellow'];
var d;
var A;
var ABAM;
var myImg;
 var nr = 0;

 plotData(x,y,value);

/**************************************/
/*Plot data*/



function plotData(x,y,myName) {

    var c;
    var mycolor=nr%color.length;
    //var t = document.getElementById('jxgbox').value;
   // var data = t.split('\n');
  

    brd.setBoundingBox([-10,maxY+10,maxX+10,-10]);
 d = brd.create('curve',[x,y],{strokeColor:color[nr%color.length],strokeWidth: 3});

    var i=0;
    do{
        i=i+1;
    } while((img[i]=="nan") && (i<(x.length-1)));
    //console.log(x.length-1) 
    
document.getElementById("BAMimg").innerHTML='<img src="BAMRAW/'+img[i]+'">';
ABAM = brd.create('glider',[x[i],y[i],d], {name:"",strokeColor:"black",fillColor:'blue',setStyle:3});
   
           
        //colorLegend.push(nr%color.length);
    A=brd.create('glider',[x[0],y[0],d], {name:'['+String(x[0])+','+String(y[0])+']', strokeColor:"black",fillColor:'white'});
  
   brd.update();
};
 
function plotMyDB(){
var value =document.getElementById("myIsothermPlot").innerHTML;
    value=value.trim();
//console.log(value);
    plotData(x,y,value);
};
 

 
    
    d.on('mousemove', function(e) {

       
         brd.removeObject(A);
        brd.removeObject(ABAM);
   var myCords= getMouseCoords(e);
        
        //Get min disst from data to mouse
        var minDist=100000000;
        var distIndex;
        var stopIfNextGreater=0;
        var prev=100000;
        for (i=0;i<x.length-1;i++) {
           var nowDist= getDistance([x[i],y[i]],myCords);
            if (nowDist<minDist){
                distIndex=i
                myX=x[i]
                myY=y[i]
                minDist=nowDist
            }
          /*
             if (prev<nowDist) { 
                 stopIfNextGreater=stopIfNextGreater+1;
             }
            else{
                stopIfNextGreater=0
            }
             if (stopIfNextGreater>4) { 
                 break; }
            prev=nowDist
            */
        }


        
          //console.log(myCords)
        
/*
        var myX=FindNearestImg(myCords[0],x);
        //var myY=FindNearestImg(myCords[1],y);
    var dist=Math.sqrt((myCords[0]*myCords[0]+myCords[1]*myCords[1]))
   var distManhatan= Math.abs(myCords[0])+Math.abs(myCords[1])
    var distNear=FindNearestImg(dist,distZero);
    var distNearManhatan=FindNearestImg(distManhatan,distZeroManhattan);
        var distIndex=distZero.indexOf(distNear)
        var distIndexManhatan=distZeroManhattan.indexOf(distNearManhatan)
        
        
        
        //console.log(myX)
        //console.log(myY)

        //var indexDataY=x.indexOf(myY);
        //var indexDataX=x.indexOf(myX);
        //Range of closests to find x and y
        myX=x[distIndex]
        myY=x[distIndex]

        myXM=x[distIndexManhatan]
        myYM=x[distIndexManhatan]
//Get which one is better
        //Error in coords
        manhatanErr=Math.abs(myXM-myCords[0])/myCords[0]+Math.abs(myYM-myCords[1])/myCords[1]
        normalErr=Math.abs(myX-myCords[0])/myCords[0]+Math.abs(myY-myCords[1])/myCords[1]
        console.log(manhatanErr,normalErr)
        if (manhatanErr<normalErr){
            myX=myXM
            myY=myYM
            distIndex=distIndexManhatan
            console.log("Manhatan")
        }
        */
         //console.log(indexData)

        
        
               var imgIndex=FindNearestImg(distIndex,imgArray);
               //var imgIndex=FindNearestImg(distIndexManhatan,imgArray);
   //brd.removeObject(ABAM);
   // ABAM = brd.create('glider',[ x[imgIndex],  y[imgIndex],d], { name:"",strokeColor:"black",fillColor:'blue'});
      
    document.getElementById("BAMimg").innerHTML='<img src="BAMRAW/'+img[imgIndex]+'">';
    
   A = brd.create('glider',[myX, myY,d], {name:'['+String(myX)+','+String(myY)+']', strokeColor:"black",fillColor:'white'});
     document.getElementById("sliderVal").value=distIndex;

       
}); 
     


function movePoint(){
        //Select the index of the data
    brd.suspendUpdate();
var indexData=Math.ceil(document.getElementById("sliderVal").value);
var myX=x[indexData];
var myY=y[indexData];
    var dist=Math.sqrt((myX*myX+myY*myY))
    //console.log("PLOT VALUES")
   
    //console.log( img)
   
//BAM image     
var imgIndex=FindNearestImg(indexData,imgArray);
   
    //console.log( imgIndex)
   brd.removeObject(ABAM);
    ABAM = brd.create('glider',[ x[imgIndex],  y[imgIndex],d], { name:"",strokeColor:"black",fillColor:'blue'});
      
    document.getElementById("BAMimg").innerHTML='<img src="BAMRAW/'+img[imgIndex]+'">';
    
         brd.removeObject(A);
       // brd.create('point', [coords.usrCoords[1], coords.usrCoords[2]]);
    A = brd.create('glider',[ myX, myY,d], {name:'['+String(myX)+','+String(myY)+']', strokeColor:"black",fillColor:'white'});
    //var point = brd.create('point', [0, 0], {withLabel: false, size: 1});


    
        brd.unsuspendUpdate();
}
   
   
function FindNearstNeighbours(){
    
}

function FindNearestImg(index,imgArray){
    var closest=imgArray.reduce(function(prev, curr) {
  return (Math.abs(curr - index) < Math.abs(prev - index) ? curr : prev);
});
    return closest;
}

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

function getDistance(firstData, secondData){
    var firstRest=firstData[0]-secondData[0]
    var secRest=firstData[1]-secondData[1]
    return Math.sqrt((firstRest*firstRest+secRest*secRest))
    
}
