
import smtplib

fromaddr = 'anthoneyblanco@gmail.com'
toaddr  = 'anthoneyblanco@yahoo.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""
messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             msg)

# Credentials (if needed)
username = 'anthoneyblanco@gmail.com'
password = 'zrcxgyvpnbnkptcx''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, messagetosend)
server.quit()
