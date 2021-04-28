

/*Load Json at start*/
var myArr;
var arrayLength;
var myArrData;
var arrayDataLength;
var dataLoaded;
 var alreadyInput=[];
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
      dataLoaded=true; 
        console.log(Object.keys(myArrData));
        var out=createFilter(myArrData,"AllNames");   
         document.getElementById("AllNamesList").style.display = "none"
      document.getElementById("AllNamesList").innerHTML=out;

      
      //var myEl = $('.Chol_B0423Xss');


    $(document).ready(function(){ 

      console.log("HOLA")
    $.getScript("/assets/functions/GraphFunctions.js");
    $.getScript("https://code.jquery.com/jquery-3.2.1.min.js");

});


  }
    else{
        console.log ("Problem with JSON for data file!! =>Stataus: " +this.status );
        dataLoaded=false;
    }
};
xmlhttpData.open("GET", "/Data/DataDB.json", true);
xmlhttpData.send(); 
    
/*
    function onDocumentClick(event) {
        var element = event.target,
            currentDataId,
            newDataId;
        console.log(element) 
    }
window.document.addEventListener("click", onDocumentClick);
*/

  
    
    /*
    jQuery.loadScript = function (url, callback) {
    jQuery.ajax({
        url: "/assets/functions/GraphFunctions.js",
        dataType: 'script',
        success: "JS LOADED",
        async: true
    });
}*/
    /*
     $(document).loadScript("/assets/functions/GraphFunctions.js");
     
     
     
$('#divForJavascript').load(document.URL +  ' #thisdiv');
var tag = document.createElement("script");
tag.src = "/assets/functions/GraphFunctions.js";


document.getElementsByTagName("body")[0].appendChild(tag);
      $.getScript("/assets/functions/GraphFunctions.js","JS LOADED");

*/
    
};
 

    function createFilter(arr,parameter){
    var str="";
    
    var allFunct="SetName( 'location','Select'); $('#location').hide()"
    var functions='onclick="myFunction">';                                                  
    for (var [key, value] of Object.entries(arr))
{
    if (alreadyInput.includes(key)==false){
 // str += "<option id='"+key+"' value='"+key+"' class='Select' "+functions+key+"</option>";
  str += "<li id='"+key+"'  class='Select'>"+key+"</li>";
        alreadyInput.push(key)
        //str=str.replaceAll("myFunction",allFunct).replaceAll("location",key);
        str=str.replaceAll("location",key);
  } 
}
   str= str.replaceAll('myParam',parameter).replaceAll("Select",parameter+"Select");
   /* str+="<script>     \
            $('.AllNamesSelect').click( function() { \
    var id = $(this).attr('id'); \
    console.log(this); \
    return false; \
}); \
    </script>"
    */
    return str;
};

