#!/usr/bin/env python
#[sever]
host="0.0.0.0" # for 0.0.0.0 all  127.0.0.1 for local 
port=20000
loglevel="DEBUG"

# same array config examples
channels=set(("channel1","channel2"))
# 生成的excel存放地址
some_path = "/tmp/some_path/"

#[MySQL]
host="mysql_host"
user="mysql_user"
passwd="mysql_passwd"
dbname="mysql_dbname"

logout="local.log"

#[Mongo]
mongo_url="mongodb://127.0.0.1:27017"
mongo_dbname="mongo_dbname"

#[Others]
#发件人邮箱
sender_email = "a@b.com"
#授权码
sender_passwd = "SENDER_PASSWD"
#收件人邮箱
recipient_email = ["c@d.com"]


#[Wechat]
wechat_appid="wxxxxxxxx"
wechat_appsecret="166xxxxxxx"
