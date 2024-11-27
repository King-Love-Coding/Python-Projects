import smtplib
from email.mime.text import MIMEText

to_number = '+918929263315@vtext.com'

from_email = 'bhativivek270@gmail.com'
from_password = 'uvwp sylf nnyi lvei'  # App Password
subject = 'Test SMS'
body = 'Hello from Python via Email-to-SMS!'


msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_number

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, to_number, msg.as_string())
    server.quit()

    print('SMS sent successfully!')
except smtplib.SMTPException as e:
    print(f'Error sending email: {e}')
