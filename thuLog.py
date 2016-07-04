import requests
username=""
key=""

def log():
  global username
  global key
  headers={'content-type' : 'application/x-www-form-urlencoded'}
  payload={'action':'login','username':username,'password':key,'ac_id':1}
  print payload
  url='https://net.tsinghua.edu.cn/do_login.php'
  r=requests.post(url,data=payload,headers=headers)
  print r.text

def read():
  global username
  global key
  f=open("account")
  username=f.readline().strip('\n')
  key='{MD5_HEX}'+f.readline().strip('\n')
  f.close()

if __name__ == "__main__":
  read()
  log()