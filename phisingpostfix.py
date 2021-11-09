import smtplib
#using postfix
SERVER = "localhost"
FROM = "root@moshe.com"
TO = ["saeed.esawi99@gmail.com"] # must be a list

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib using postfix"

# Prepare actual message
message = """\
From: %s
To: %s
Subject: %s
%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()
