import socket
import smtplib
from email.mime.text import MIMEText
to = 'michaeldelcid16@gmail.com' # Email to send to
gmail_user = 'michaeldelcid16@gmail.com' # Email to send from (MUST BE GMAIL)
gmail_password = 'GMAIL_PW' # Turn on 2-Step Verification and generate 16-digit App Password
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)
ipaddr = socket.gethostbyname(socket.gethostname())
my_ip = 'HOSTNAME IP address is %s' % ipaddr # Change HOSTNAME
msg = MIMEText(my_ip)
msg['Subject'] = 'IP address for HOSTNAME' # Change HOSTNAME
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
