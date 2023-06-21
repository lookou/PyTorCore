import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from llog import llogger
import conf

logger = llogger()

def SendEmail(excel_name):
  msg = MIMEMultipart()
  msg["From"] = Header(conf.sender_email, "utf-8")
  msg["To"] = Header(",".join(conf.recipient_email), "utf-8")
  msg["Subject"] = Header("Panid相似用户", "utf-8")
  # 构造附件
  att = MIMEText(open(excel_name, "rb").read(), "base64", "utf-8")
  att["Content-Type"] = 'application/octet-stream'
  # 设置附件信息
  att["Content-Disposition"] = "attachment; filename = \"{}\"".format(excel_name)
  msg.attach(att)
  
  # 给其他邮箱发邮件要用非SSL端口
  # smtp = smtplib.SMTP("smtp.163.com", 25)
  smtp = smtplib.SMTP_SSL("smtp.163.com", 465)
  smtp.login(conf.sender_email, conf.sender_passwd)
  smtp.sendmail(conf.sender_email, conf.recipient_email, msg.as_string())
  logger.debug("邮件发送成功")
