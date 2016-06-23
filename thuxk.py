#!/usr/bin/
# coding:utf-8

import requests
from PIL import Image
from StringIO import StringIO

#初始化session
s=requests.Session()
#获取cookie
s.get('http://zhjwxk.cic.tsinghua.edu.cn/xklogin.do')

#获取二维码并且打开，人工判断。。。
r=s.get('http://zhjwxk.cic.tsinghua.edu.cn/login-jcaptcah.jpg?captchaflag=login1')
i=Image.open(StringIO(r.content))
i.show()
ewm=raw_input(">>>")

#设置首部和body，请填写账号密码
payload={'j_username':'','j_password':'','captchaflag':'login1','_login_image_':ewm}
h={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36','referer':'http://zhjwxk.cic.tsinghua.edu.cn/xklogin.do','origin':'http://zhjwxk.cic.tsinghua.edu.cn','content-type': 'application/x-www-form-urlencoded'}

#post并且打印登录成功页面
r=s.post('https://zhjwxk.cic.tsinghua.edu.cn/j_acegi_formlogin_xsxk.do',data=payload,headers=h)
print r.content
