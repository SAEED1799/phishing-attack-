import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmailUser = 'esawisaeed0@gmail.com'
gmailPassword = 'saeed1799'
recipient = 'saeed.esawi99@gmail.com'

message = f"""
join and recieve 1000 NIS gift...
"""

msg = MIMEMultipart()
msg['From'] = f'"Your Name" <{gmailUser}>'
msg['To'] = recipient
msg['Subject'] = "fox clothes"
msg.attach(MIMEText(message))

try:
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmailUser, gmailPassword)
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    mailServer.close()
    print ('Email sent!')
except:
    print ('Something went wrong...')