#!/usr/bin/env python

import smtplib, sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "enter from address"
toaddr = "enter to address"
msg = MIMEMultipart()
#msg['From'] = 'enter from address'
#msg['To'] = 'enter to address'
#msg['Subject'] = "enter subject line""
 
body = str(sys.argv[1])
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('enter email server', 587)
server.starttls()
server.login("username", "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
