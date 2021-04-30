
console.log("functions.js")
/***********************************************/
/*Function to show list possible names*/
//console.log(document.getElementsByClassName("NameSelect"))
/*
document.querySelectorAll(".NameSelect").forEach(item => {
 var key;
   //console.log(item)
    item.addEventListener("click",function(){
      console.log("Pro") 
      key=item.id;
      console.log(item+" " +key)  
      
      SetName(key,"SuggestedNameSelect");
      item.style.display = "none";
    //document.getElementById("nameFind").value="";
    });
    }); 
*/


/***************************/
/* Send all chooses to text box*/

addListenerToDropList("Substance1Suggest");
addListenerToDropList("TemperatureSuggest");
addListenerToDropList("SpeedSuggest");
//addListenerToDropLis(["Substance1Select"]);

function addListenerToDropList(label){
 
       
 label=label.replace("Suggest","Select"); 
       //console.log(label)
       document.querySelectorAll("."+label).forEach(item => {
 var key;
         
    item.addEventListener("click",function(){
       
      //console.log("Pro")
      key=item.id;
      //console.log(item+" " +key)
      
      SetName(key,String(label),true);
      item.style.display = "none"; 
console.log(label) 
    });
    });  
    
}  

 
function ShowNames() {
    
    var name =document.getElementById("nameFind").value;
     console.log(name)
    if (name.length<1){ console.log("This")
        }
 
    /*Get list of matches*/
    console.log(document.getElementById("SuggestedNameSelect"))
    var alreadyFound=document.getElementById("SuggestedNameSelect").textContent;
    var myList=FindSuggest("NameSelect",alreadyFound);
       console.log(name)
    //console.log("Textarea two was changed. =>"+name+myList);
   
           
};

document.getElementById("nameFind").addEventListener('keyup', ShowNames);  //When pressing key



/******************/
/*Collapsible div*/



document.getElementById("Namecollapsible").addEventListener("click",function(){
    var mySibling=document.getElementById("NameSuggest")
    //console.log(mySibling.style.display)
if (mySibling.style.display == "block"){
    mySibling.style.display = "none"
}else{
    console.log("HERE")
    ShowNames()
    mySibling.style.display = "block";
}
});

/*
document.querySelectorAll(".dataFilterul").forEach(myList =>{
    myList.addEventListener("click",function(){
        //var myList=item.getElementById("dataFilterul")
    //console.log(mySibling.style.display)
if (myList.style.display == "block"){
    myList.style.display = "none"
}else{
    
    myList.style.display = "block";
}
});
});

*/

document.querySelectorAll('.NameSelect').forEach(item => {

 var key;
          
    item.addEventListener("click",function(){
        
      console.log("Pro")
      key=item.id;
      //console.log(item+" " +key)
      
      SetName(key,"SuggestedNameSelect");
      item.style.display = "none"; 
//console.log(label) 
    });
    });  
    

/*Search button*/

document.getElementById("SearchData").addEventListener("click",function(){
    submitSearch();
    setTimeout(() => {  clearAll(); }, 500);
  
});
document.getElementById("ClearAll").addEventListener("click",function(){
     clearAll();
});

/*Drop down buttons*/

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
    });    


//Erase buttons listener
document.querySelectorAll('.RemoveButton').forEach(item => {
 var key;
    item.addEventListener("click",function(){
      //console.log("Pro")
      key=item.id.replace("Remove","Select");
   // console.log(item+" " +key)
      eraseText(key)
        this.stopPropagation;
//if (key!="NameSelect"){ 
//    $('.'+key).show()
//}
    });
    });






/*****************************************/
/* FIlter the data */

function submitSearch(){
    console.log("HEREE")
    console.log(document.getElementById("SuggestedNameSelect"))
    var filter = {};
    var filterIn = {};
    
    var filterOut=JSON.parse(JSON.stringify(myArr));
   
    var arrayOutLength = Object.keys(filterOut).length;
    var arrayOutKeys= Object.keys(filterOut);
    
    
    filter["Name"] =document.getElementById("SuggestedNameSelect").textContent.split(",");
    filter["Temperature"] =document.getElementById("TemperatureSelect").value.split(",");
    filter["Substance1"] =document.getElementById("Substance1Select").value.split(",");
    filter["Speed"] =document.getElementById("SpeedSelect").value.split(",");
    
     
    var filterStartDate =document.getElementById("startDate").value;
    var filterEndDate =document.getElementById("endDate").value;

    //filter["subfase"] =document.getElementById("subfase").value;
    
    console.log(document.getElementById("SuggestedNameSelect").textContent)
    //First get time range
    var filterTime=2;
    if (filterStartDate== null || filterStartDate == "" || filterStartDate == "any"){
            console.log("no Start Date")
        filterStartDate="0000-01-01"
        filterTime=filterTime-1;
        }
    if (filterEndDate== null || filterEndDate == "" || filterEndDate == "any"){
            console.log("no End Date")
        filterEndDate="5000-01-01"
        filterTime=filterTime-1;
        }
    filterStartDate=parseDate(filterStartDate);
    filterEndDate=parseDate(filterEndDate);
    if (filterTime!=0){
         for (var i of arrayOutKeys.values()) {
             var myDate= new Date(filterOut[i]["Date"]);
              //console.log(myDate+" ............."+filterStartDate)
             
              //console.log(myDate>=filterStartDate)
             if ((myDate>=filterStartDate) && (myDate<=filterEndDate))
        {filterIn[i]=JSON.parse(JSON.stringify(filterOut[i]));
                                         console.log("Assign")};
             
         }
           filterOut = JSON.parse(JSON.stringify(filterIn));
    arrayOutLength = Object.keys(filterOut).length;
    arrayOutKeys= Object.keys(filterOut); 
    
    }

    for (const [key, value] of Object.entries(filter)) {
        filterIn = {};
        console.log(key);
        console.log(value);
         if (arrayOutLength == 0) { break; }
    //Remove not given values
        if ((Object.keys(value).length==1) && ((value[0] == null || value[0] == "" || value[0] == "any"))){
            console.log("nodata")
        }
        else{
           
            for (const value2 of value){    //Several values for each type
                //console.log(filterOut);
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
                                         console.log("Assign")};
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





function FindSuggest(classLi,findThis,alreadyFound){
        if (findThis.length<1){
        return 
    }
    /*ulItem is the ul list*/
    //Parameter => what parameter to compare
   findThis= findThis.toUpperCase();
   alreadyFound= alreadyFound.toUpperCase();
var srt = "";
    var found=false;
    var tempstr=[];     //Items to remove


    console.log(findThis)
    document.querySelectorAll("."+classLi).forEach(myList =>{
       
if ((value.toUpperCase().indexOf(findThis)<0) || (alreadyFound.indexOf(value.toUpperCase())>=0)){
    myList.style.display="none";
}
        else{
            myList.style.display="block";
            found=true
        }
  })

        if (!found){
         document.getElementById("noMatchesName").style.display="block";
        }
else{
      document.getElementById("noMatchesName").style.display="none";
}
    console.log(document.getElementById(classLi.replace("Select","Suggest")))
    document.getElementById(classLi.replace("Select","Suggest")).style.display="block"
return;
    };



/*******************************************/
/* Insert selection*/
function SetName(location,output,fromList=false) {
    if (fromList==false){
        var textOut=document.getElementById(location).textContent;
    }
    else{
         var textOut=location;
        
    }
      var txtName = document.getElementById(output);
    console.log(output)

    if (txtName.value ==""){
        txtName.value =textOut;

    }
    else{
              txtName.value = txtName.value.concat(", "+textOut);
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
    document.getElementById(suggestions).style.display="none";
    eraseText(inputID);
    
    
}


function clearAll(){
    document.getElementById("SuggestedNameSelect").textContent="";
    document.getElementById("Substance1Select").value="";
    document.getElementById("SpeedSelect").value="";
    document.getElementById("TemperatureSelect").value="";
    document.getElementById("startDate").value=null;
    document.getElementById("endDate").value=null;
    var out=createDiv(myArr);
    document.getElementById("isotherm_button_in").innerHTML=out;
    
}

