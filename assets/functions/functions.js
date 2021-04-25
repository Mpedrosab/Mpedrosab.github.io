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
    //Create Substance selection
    var out=createFilter(myArr,"Substance1");   
    document.getElementById("suggestionsSub").innerHTML=out;
    out=createFilter(myArr,"Temperature");     
    document.getElementById("suggestionsTemp").innerHTML=out;
    out=createFilter(myArr,"Speed");     
    document.getElementById("suggestionsSpeed").innerHTML=out;

  }
    else{
        console.log ("Problem with JSON file!! =>Stataus: " +this.status );
        
    }
};

xmlhttp.open("GET", "/borrar.json", true);
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
    filter["name"] =document.getElementById("NameSelect").value;
    filter["temp"] =document.getElementById("TemperatureSelect").value;
    filter["substance"] =document.getElementById("Substance1Select").value;
    filter["vel"] =document.getElementById("SpeedSelect").value;
    
    filter["startDate"] =document.getElementById("startDate").value;
    filter["endDate"] =document.getElementById("endDate").value;

    //filter["subfase"] =document.getElementById("subfase").value;
    //Remove not given values
    for (const [key, value] of Object.entries(filter)) {
        if (key=="substance"){
            
        }
    if (value == null || value == "" || value == "any"){
        filter[key]="";
    }
    }
    
    //Filter data
    console.log(filter)
    
   // arrOut=filter(myArr,name);
        var out =jQuery.grep(myArr,function(element,index){
            var myout=true;
             //myout = element.Name==name;
            //console.log(myArr[0].Name==name)
            return element.Name==name;
            
                if (name != null && name != ""){
                myout = element.Name==name;
                if (myout==false){return myout;}    
                
            }
            return myout; 
            
          

                           
                            });
    console.log("The is "+arrayLength )

    
for (var i = 0; i < arrayLength; i++) {
   // console.log(myArr[i].Name)
    //Do something
}

};

/**************************************************/

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