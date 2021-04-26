
var brd = JXG.JSXGraph.initBoard('jxgbox',{boundingbox:[-1,5000,25,-400],axis:true});
var color = ['blue','red','magenta', 'green', 'black','yellow'];
var nr = 0;
var maxX = 0.0;
var maxY = 0.0;
var minY = 100000.0;

function plotData(data) {
    var i;
    var x=data[0];
    var x=data[1];
    
    //var t = document.getElementById('jxgbox').value;
   // var data = t.split('\n');
    for (i=0;i<x.length-1;i++) {
        //d = data[i].split(';');
        //x[i] = d[0]*1.0;
        //y[i] = d[1]*1.0;
        if (x[i]>maxX) maxX = x[i];
        if (y[i]>maxY) maxY = y[i];
        if (y[i]<minY) minY = y[i];
    }
    brd.setBoundingBox([-1,maxY*1.01,maxX*1.05,minY*0.95]);
    var c = brd.create('curve',[x,y],{strokeColor:color[nr%color.length]});
    nr++;
    brd.update();
};

function loadData(value){
    var myDiv= document.getElementById('hiddenData');
   
    myDiv.load("/"+value["HTML"]);
   

    /*
    document.getElementById('hiddenData').innerHTML='<iframe class="myName" src="/myHTML" style="display:none"></iframe>'.replace("myHTML",value["HTML"]).replace("myName",value["Name"]);
*/
};


function readData(value){
        loadData(value); //Load the html in a hidden location
    //var oTable = document.getElementsByClassName('dataframe')
     var oTable = document.getElementsByClassName('dataframe isotherm_data')[0];

    console.log(oTable)
    //gets rows of table
    var rowLength = oTable.rows.length;

    //loops through rows    
    for (i = 0; i < rowLength; i++){

      //gets cells of current row  
       var oCells = oTable.rows.item(i).cells;

       //gets amount of cells of current row
       var cellLength = oCells.length;

       //loops through each cell in current row
       for(var j = 0; j < cellLength; j++){

              // get your cell info here

              var cellVal = oCells.item(j).innerHTML;
              alert(cellVal);
           }
    }
    
}

var value={}
value["HTML"]="Data/Chol_B0423Xss/Chol_B0423Xss_tuned.html";
value["Name"]="n";
readData(value);