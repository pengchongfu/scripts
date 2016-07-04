var request=require('request');
var uname = "用户名";
var pass = "密码";
var ac_id = "1";
var crypto = require('crypto');
pass = crypto.createHash('md5').update(pass).digest('hex');//md5加密

var topost = "action=login&username=" + uname + "&password={MD5_HEX}" + pass + "&ac_id="+ac_id;

process.argv[2]==="1"?void(0):topost = "action=logout";//获取命令行参数决定login还是logout

request.post({
  headers: {'content-type' : 'application/x-www-form-urlencoded'},
  uri:'https://net.tsinghua.edu.cn/do_login.php',
  body:topost
},function(err,res,body){
  console.log(body);
});