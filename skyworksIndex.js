var FormData=require("form-data");
var fs=require('fs');
var request=require('request');

var formdata = {
  name: "pcf",
  email:"pcf@pcf.com",
  title:"标题",
  description:"<p>描述</p>",
  url:"",
  file:fs.createReadStream(__dirname + '/filename')//the file
  
}

function sendFile(){
  request({
  uri:'https://media.thu-skyworks.org/upload/submit',
  method:'POST',
  formData:formdata,
},function(err,res,body){
  console.log(res+body);
});
}

sendFile();