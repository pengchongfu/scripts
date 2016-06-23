#!/usr/bin/python
#-*- coding:utf-8 -*-

import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#从rcontact表中获取联系人的nickname（对方自定义的昵称），conRemark（我方备注的昵称），username（微信标识用户的字符串）
#并且保存在字典中，键为username，值为昵称（conRemark优先）
def getContact(contact):
        cursor = conn.execute("select username,conRemark,nickname from rcontact")
        for row in cursor:
                name=''
                if row[1]:
                        name=row[1]
                elif row[2]:
                        name=row[2]
                contact[row[0]]=name

#从rcontact表中根据微信群名获取微信群的username
def getChatroom():
        chatroom=sys.argv[1]#命令行得到的参数
        cursor = conn.execute("select nickname,username from rcontact")
        for row in cursor:
                if row[0] == chatroom:
                        return row[1]
                        
#从message表中获取属于特定微信群的消息，并且将username替换成之前获得的昵称
#并且输出到屏幕上
def getMessage():
        cursor = conn.execute("select talker,content from message")
        for row in cursor:
                if chatroom == row[0]:
                        username = (row[1].split(":"))[0]
                        if contact.get(username):
                                username=contact.get(username)
                        message = (row[1].split(":"))[1]
                        print username,message,'\n'
        

conn = sqlite3.connect('decrypted_database.db')#打开数据库

contact = {}
getContact(contact)
chatroom = getChatroom()
getMessage()

conn.close()#关闭数据库
