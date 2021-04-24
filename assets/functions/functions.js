
function sub(){

    
   var output= $.ajax({
        url: 'Params.csv',
        dataType: 'text',
      }).done(successFunction);

};


    function successFunction(data) {
        var allRows = data.split(/\r?\n|\r/);
        var header=allRows[0].replace('"','').split(",");
        
       var output;
         for (var singleRow = 0; singleRow < allRows.length; singleRow++) {
             output+="<p>"+allRows[singleRow]+"</p>"
         
        
    }
        document.getElementById("demo").innerHTML=header;
    };