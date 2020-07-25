# coding:utf-8
import smtplib
from email.mime.text import MIMEText
import os
import yaml
#读取yaml数据

# 获取当前文件路径
filePath = os.path.dirname(__file__)
print(filePath)
# 获取当前文件路径
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
print(fileNamePath)
# 获取数据文件的路径
yamlPath = os.path.join(fileNamePath,'loginYaml.yaml')

f = open(yamlPath,'r',encoding='utf-8')
#文件读取
cont = f.read()
#用load方法转字典
x = yaml.load(cont, Loader=yaml.FullLoader)


# ----------1.跟发件相关的参数------
# smtpserver = "smtp.163.com"         # 发件服务器
smtpserver = "smtp.qq.com"
port = 465                                        # 端口
sender = x['user2']         # 账号
psw = x['pwd']                       # 密码
receiver = x['user1']        # 接收人

# ----------2.编辑邮件的内容------
subject = "这个是主题QQ"
body = '<p>这个是发送的QQ邮件</p>'     # 定义邮件正文为html格式
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = receiver
msg['subject'] = subject

# ----------3.发送邮件------
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)                                 # 连服务器
smtp = smtplib.SMTP_SSL(smtpserver, port)
smtp.login(sender, psw)                                      # 登录
smtp.sendmail(sender, receiver, msg.as_string())  # 发送
smtp.quit()                                                        # 关闭
