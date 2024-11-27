# import smtplib
# # creates SMTP session
# s = smtplib.SMTP('smtp.gmail.com', 587)
# # start TLS for security
# s.starttls()
# # Authentication
# s.login("bhativivek270@gmail.com", "Bharat@15")
# # message to be sent
# message = "hii"
# # sending the mail
# s.sendmail("bhativivek270@gmail.com", "jvvasita@yahoo.com", message)
# # terminating the session
# s.quit()


import yagmail

# initiating connection with SMTP server
yag = yagmail.SMTP("bhativivek270@gmail.com",
                   "Bharat@15")
# Adding Content and sending it
yag.send("jvvasita@yahoo.com",
         "casual",
         "(Text)")

