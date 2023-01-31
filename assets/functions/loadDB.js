var ajax_request = new XMLHttpRequest();

ajax_request.open('GET', 'assets/functions/readDB.php');
//ajax_request.setRequestHeader("Accept-Encoding", "UTF-8");
    	var queryData=new FormData();
	//queryData_val=encodeURI(queryData_val);
		//queryData.append("query","SELECT * FROM Data");
		queryData.append("query","SELECT * FROM Params");

ajax_request.send(queryData);
ajax_request.onreadystatechange = function()
	{
		if(ajax_request.readyState == 4 && ajax_request.status == 200)
		{ 
			console.log("OK");
			console.log(ajax_request.response);
        }
    else{
        console.log ("Problem with JSON file!! =>Stataus: " +this.status );
        
    }
}