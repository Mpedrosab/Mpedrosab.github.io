    var request = new XMLHttpRequest();
    request.open('GET', 'https://github.com/matteobrusa/Password-protection-for-static-pages/blob/master/README.md', true);
    request.send(null);
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            var type = request.getResponseHeader('Content-Type');
            if (type.indexOf("text") !== 1) {
               alert(request.responseText);
            }
        }
    }


function EncryptEmail(keyEmail){
  mycoded=keyEmail
  key = "073gJ94PRqXTpwWaDsHKULvCrEYQOIebSNumcz5FG8VB1txMyfjhiZ2klndo6A"
  shift=mycoded.length
  link=""
  for (i=0; i<mycoded.length; i++) {                          
    if (key.indexOf(mycoded.charAt(i))==-1) {                 //If letter is not in key, give the same character as in code
       
      ltr = mycoded.charAt(i).replace("@","-").replace(".","_")
      link += (ltr)
      
    }                           
    else {                                                                  
        /*Gets the position in key of every char  at coded. Ex. if key=longm5s7h2587 and coded=nobot@yeah it gives 
            n => position in key: 2
            key length: 13
            code length= shift: 10
            ltr=(2-10+13)%13=5%13=8       //% gives the remainder
        */
      ltr = (key.indexOf(mycoded.charAt(i))-shift+key.length) % key.length
      link += (key.charAt(ltr))
    }
    //console.log(key.indexOf(mycoded.charAt(i)))
  }
    console.log(link)
  return link;
}