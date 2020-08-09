import smtplib
server = smtplib.SMTP('smtp.gmail.com',25)
server.ehlo(name='Server is up !!!')
