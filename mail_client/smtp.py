import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com',25)
server.ehlo(name='Server is up !!!')
with open ('password.txt','r') as f:
    password = f.read()
request = server.login('asimsaeed74@gmail.com',password)    


msg = MIMEMultipart()
msg['From'] = 'Python sockets'
msg ['To']  = 'asimsaeed74@gmail.com'
msg ['Subject'] = 'Sockets TEST'

with open('Message.txt','r') as f:
    Message  = f.read()

msg.attach(MIMEText(Message,'plain'))

file_name  =  'attachment.png'

attachment = open(file_name,'rb') 

p = MIMEBase('application','octet-stream')

p.set_payload(attachment.read())
encoders.encode_base64(p)

p.add_header('Content-Dispostion',f'attachment; filename={attachment}')
msg.attach(p)

text  = msg.as_string()

server.sendmail('asimsaeed74@gmail.com','asimsaeed74@gmail.com',text)