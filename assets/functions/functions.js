/*Load Json at start*/
var myArr;
var arrayLength;


/*****************************************/
window.onload = function () {
var xmlhttp = new XMLHttpRequest();
//fetch( "/borrar.json").then(response => response.json())

//console.log(response)

xmlhttp.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
      console.log("Good");
  myArr = jQuery.parseJSON(this.responseText);
      arrayLength = Object.keys(myArr).length;
      console.log(myArr);
    //Create  selections
    var out=createFilter(myArr,"Substance1");   
    document.getElementById("suggestionsSub").innerHTML=out;
    out=createFilter(myArr,"Temperature");     
    document.getElementById("suggestionsTemp").innerHTML=out;
    out=createFilter(myArr,"Speed");     
    document.getElementById("suggestionsSpeed").innerHTML=out;

      //Create Div
      out=createDiv(myArr);
      document.getElementById("isotherm_button_in").innerHTML=out;
  }
    else{
        console.log ("Problem with JSON file!! =>Stataus: " +this.status );
        
    }
};

xmlhttp.open("GET", "/Data/ParamsDB.json", true);
xmlhttp.send(); 
    
     $('#suggestionsName').hide(); //Hide name suggestins
    

    
};


/***********************************************/
/*Function to show list possible names*/
$('#nameFind').keyup( function(e) {
    
   var t = e.keyCode;
    var name =document.getElementById("nameFind").value;
    
    if (name==""){ $('#suggestionsName').hide();
        }
   else{
    /*Get list of matches*/
    var alreadyFound=document.getElementById("NameSelect").value;
    var myList=FindSuggest(myArr,name,"Name",alreadyFound);
    //console.log("Textarea two was changed. =>"+name+myList);
   $('#suggestionsName').show();
    $('#suggestionsName').html(myList);
   }
           
});

function FindSuggest(array,findThis,parameter,alreadyFound){
    //Parameter => what parameter to compare
   findThis= findThis.toUpperCase();
   alreadyFound= alreadyFound.toUpperCase();
var srt = "<ul>";
    var found=false;
    
for (var [key, value] of Object.entries(array))
{
  //console.log(value[parameter]+"=>"+alreadyFound.indexOf(value[parameter].toUpperCase())+"=>"+value[parameter].toUpperCase().indexOf(findThis));
    if ((value[parameter].toUpperCase().indexOf(findThis)>=0) && (alreadyFound.indexOf(value[parameter].toUpperCase())<0)){
        srt += "<li class='suggestion_name' id='suggestion_name' onclick='"+'SetName("suggestion_name","NameSelect"); ClearSuggest("suggestionsName","nameFind")'+"'>" + value[parameter] + "</li>";
        found=true;
    }
    

    }
        if (!found){
         srt += "<li>No matches found!!</li>";
        }
srt += "</ul>";
return srt;
    };


/**************************************/

/* Function to add suggestion on click*/
/*
var something = document.getElementById('suggestion_name');
something.onclick=SetName("suggestion_name","name");
*/
    

/*****************************************/
/* FIlter the data */

function sub(){
    var filter = {};
    var filterIn = {};
    
    var filterOut=JSON.parse(JSON.stringify(myArr));
   
    var arrayOutLength = Object.keys(filterOut).length;
var arrayOutKeys= Object.keys(filterOut);
    filter["Name"] =document.getElementById("NameSelect").value.split(",");
    filter["Temperature"] =document.getElementById("TemperatureSelect").value.split(",");
    filter["Substance1"] =document.getElementById("Substance1Select").value.split(",");
    filter["Speed"] =document.getElementById("SpeedSelect").value.split(",");
    
     
    var filterStartDate =document.getElementById("startDate").value;
    var filterEndDate =document.getElementById("endDate").value;

    //filter["subfase"] =document.getElementById("subfase").value;
    

    for (const [key, value] of Object.entries(filter)) {
        filterIn = {};
        console.log(key);
         if (arrayOutLength == 0) { break; }
    //Remove not given values
        if ((Object.keys(value).length==1) && ((value[0] == null || value[0] == "" || value[0] == "any"))){
            console.log("nodata")
        }
        else{
           
            for (const value2 of value){    //Several values for each type
                console.log(filterOut);
                /*
                var filteredIn= filterOut.filter(function(e) {
                return e[key] == value2;
                });
                */
               console.log(arrayOutKeys)
            for (var i of arrayOutKeys.values()) {
            console.log(i)
             //myout = element.Name==name;
            
            if(filterOut[i][key]==value2){filterIn[i]=JSON.parse(JSON.stringify(filterOut[i]));
                                         console.log("Assin")};
        };
                
       }
           //  console.log(filterOut)
        //console.log(filterIn);
       filterOut = JSON.parse(JSON.stringify(filterIn));
        arrayOutLength = Object.keys(filterOut).length;
        arrayOutKeys= Object.keys(filterOut);
    }

    };
            
       
    //Create div with data
    if (arrayOutLength>0){
         var codeOut = createDiv(filterOut);
    }
   else{
       var codeOut = "<h3>No data found! :( </h3>"
   }
    document.getElementById("isotherm_button_in").innerHTML=codeOut;
    console.log("The is "+arrayLength )
    console.log(filterOut )
    
    
    
    

};

/**************************************************/
/*Create filter for header page*/
function createFilter(arr,parameter){
    var str="<option value='any'>Any</option>";
    var alreadyInput=[];
    var allFunct="SetName( 'location','Select'); $('#location').hide()"
    var functions='onclick="myFunction">';                                                 
    for (var [key, value] of Object.entries(arr))
{
    if (alreadyInput.includes(value[parameter])==false){
  str += "<option id='"+value[parameter]+"' value='"+value[parameter]+"' class='Select' "+functions+value[parameter]+"</option>";
        alreadyInput.push(value[parameter])
        str=str.replaceAll("myFunction",allFunct).replaceAll("location",value[parameter]);
  }
}
   str= str.replaceAll('myParam',parameter).replaceAll("Select",parameter+"Select");

    console.log(allFunct)

    //+
            
    console.log("create filter");
    return str;
};


/*Create div with data*/
 function createDiv(arr){
        var str='<div class="overlay">\
            <img src="/myIMG" class="button"><div class="button"><a href="/myHTML" class="button"><h2 class="button">mySubstance</h2><br>Date: myDate<br>V= myVol myVolUnit [myConc myUnitConc]<br>T= myTemp °C; speed= mySpeed myUnitSpeed</a></div>\
        </div>\
          '
     var strOut="";
      for (const [key, value] of Object.entries(arr)){
                      
          strOut+=str.replace("myIMG",value["IMG"]).replace("myHTML",value["HTML"]).replace("mySubstance",value["Substance1"]).replace("mySubstance",value["Substance1"]).replace("myVol",value["Volume1"]).replace("myVolUnit",value["Unit_Vol"]).replace("myUnitConc",value["Unit1"]).replace("myConc",value["Concentration1"]).replace("myTemp",value["Temperature"]).replace("mySpeed",value["Speed"]).replace("myUnitSpeed",value["Unit_Speed"])
          
      }
     return strOut;
     
 };


/*******************************************/
/* Insert selection*/
function SetName(location,output) {
      var txtName = document.getElementById(output);
    //console.log(document.getElementById(output).textContent)
      /*txtName.value = Array.prototype.filter.call( document.getElementById(location).textContent, el => el).map(el => el).join(",");*/
    if (txtName.value ==""){
        txtName.value =document.getElementById(location).textContent;

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

/************************************/
/* Hide suggestion and clear input*/
function ClearSuggest(suggestions,inputID){
    $('#'+suggestions).hide();
    eraseText(inputID);
    
    
}


function clearAll(){
    document.getElementById("NameSelect").value="";
    document.getElementById("Substance1Select").value="";
    document.getElementById("SpeedSelect").value="";
    document.getElementById("TemperatureSelect").value="";
    document.getElementById("startDate").value=null;
    document.getElementById("endDate").value=null;
    var out=createDiv(myArr);
    document.getElementById("isotherm_button_in").innerHTML=out;
    
}

