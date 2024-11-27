# from django.core.mail.backends import smtp
# import datetime
# import sendsms
# import pandas as pd
# from pandas import *
# import datetime
# import smtplib     #simple mail transfer protocol libraries(smtplib)
# import time
# import requests
# from win10toast import ToastNotifier
# from twilio.rest import TwilioRestClient
# import request
# from request import PandaRequest
# # import project
# from BirthdayGmail import *
#
# # import project
# if __name__ == "__main__":
#     dataframe = pd.read_excel("BirthdayChart.xlsx")            #read excel file in panda format
#     today = datetime.datetime.now().strftime("%d-%m")          #string format time(strftime)
#     yearNow = datetime.datetime.now().strftime("%Y")
#     writeInd = []
#     for index, item in dataframe.iterrows():
#         msg = "Happiest Birthday To You"+str(item["NAMES"])
#         bday = item['Birthday'].strftime("%d-%m")
#
#         if (today == bday) and yearNow not in str(item['DATE OF BIRTH']):
#             sendEmail(item['Gmail ID'], "Happy Birthday", msg)
#             sendsms(item['Contact Number'], msg, item['NAMES'],"Happy Birthday")
#             writeInd.append(index)
#
#     dataframe.to_excel('BirthdayChart.xlsx',index=False)




import datetime

import pandas as pd
import sendsms

from BirthdayGmail import sendEmail  # Assuming these are your custom functions

if __name__ == "__main__":
    # Read the Excel file containing birthdays
    dataframe = pd.read_excel("BirthdayChart.xlsx")

    # Get today's date in day-month format
    today = datetime.datetime.now().strftime("%d-%m")
    year_now = datetime.datetime.now().strftime("%Y")

    write_ind = []

    # Iterate over each row in the dataframe
    for index, item in dataframe.iterrows():
        msg = f"Happiest Birthday To You " + item['Name']
        bday = item['Date of Birth'].strftime("%d-%m")

        # Check if today is the birthday and if the message hasn't been sent this year
        if today == bday:
            sendEmail(item['GMAIL ID'], "Happy Birthday", msg)
            sendsms(item['Contact Number'], msg, item['Name'], "Happy Birthday")
            write_ind.append(index)

    # Update the Excel file to mark birthdays for which greetings have been sent
    dataframe.to_excel('BirthdayChart.xlsx', index=False)



