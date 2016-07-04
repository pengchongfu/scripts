var FormData=require("form-data");
var fs=require('fs');
var request=require('request');

var cookie;//保存cookie

request({
  url:'your url',
  method:'POST',
  form:{
    login:'your username',
    password:'your password'
  }
},function(err,res,body){
  cookie = res.headers['set-cookie'];
  console.log(cookie);
  sendFile();
});

var formdata = {
  file: fs.createReadStream(__dirname + '/*.pdf')//the file
}

function sendFile(){
  request({
  uri:'your sendfile url',
  method:'POST',
  headers:{
    Cookie:cookie,
  },
  formData:formdata,
},function(err,res,body){
  console.log(body);
});
}