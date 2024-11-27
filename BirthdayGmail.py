# from django.core.mail.backends import smtp
# import datetime
# import sendsms
# import pandas as pd
# from pandas import *
# import datetime
# import smtplib     #simple mail transfer protocol libraries(smtplib)
# from win10toast import ToastNotifier
# from twilio.rest import TwilioRestClient
# import request
# from request import PandaRequest
#
#
#
# GMAIL_ID ='bhativivek270@gmail.com'
# GMAIL_PWD = 'bharat@15'
#
# toast = ToastNotifier()      # To give a notification on desktop
#
# def sendEmail(to,sub,msg):
#       email_obj = smtplib.SMTP('smtp.gmail.com',266)
#       email_obj.starttls()                   #Transport Layer Security (TLS) protocol in order to encrypt the information
#                                            # transmitted using the TLS protocol.
#                                            #also known as STARTSSL, StartSSL or “Opportunistic TLS”
#
#       email_obj.login(GMAIL_ID, GMAIL_PWD)
#       email_obj.sendmail(GMAIL_ID,to,f"Subject:{Wish}\n\n{HappyBirthday}")
#
#       email_obj.quit()
#       print("Email Sent To :"+str(to)+"with Subject :"+str(sub)+"And Message :"+str(msg))
#       toast.show_toast("E-mail Sent!!!","{Happy Birthday} was sent e-mail",threaded=True,icon_path=none,duration=6)
#     #Threading allows you to have different parts of your process run concurrently
#
# while toast.notification_active():
#         time.sleep(0.1)
#


import smtplib
import datetime
import pandas as pd
from win10toast import ToastNotifier
from twilio.rest import Client  # Twilio API for SMS
import time

# Gmail credentials
GMAIL_ID = 'bhativivek270@gmail.com'
GMAIL_PWD = 'uvwp sylf nnyi lvei'  # Use an app-specific password, not your regular Gmail password

# Initialize ToastNotifier for desktop notifications
toast = ToastNotifier()


def sendEmail(to, sub, msg):
      try:
            # Create an SMTP session
            email_obj = smtplib.SMTP('smtp.gmail.com', 587)  # Use port 587 for TLS
            email_obj.starttls()  # Start TLS for security

            # Login to Gmail
            email_obj.login(GMAIL_ID, GMAIL_PWD)

            # Send email
            email_obj.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
            email_obj.quit()

            print(f"Email Sent To: {to} with Subject: {sub} And Message: {msg}")

            # Show notification on the desktop
            toast.show_toast("E-mail Sent!!!", f"{msg} was sent via email", threaded=True, icon_path=None, duration=6)

      except Exception as e:
            print(f"Failed to send email: {str(e)}")
            toast.show_toast("E-mail Failed", f"Failed to send email to {to}", threaded=True, icon_path=None,
                             duration=6)


# Wait until the toast notification is no longer active
while toast.notification_active():
      time.sleep(0.1)

