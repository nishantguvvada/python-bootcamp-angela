# Email SMTP (Simple Mail Transfer Protocol) and datetime module

import smtplib
from dotenv import load_dotenv
import os
import datetime
import random

load_dotenv()

my_email = "nishant.guvvada@gmail.com"
password = os.getenv('PASSWORD')

try:
    with open("quotes.txt", "r") as quotes:
        quote_list = quotes.readlines()
except:
    print("File Not Found")
else:
    today = datetime.datetime.now().weekday()
    final_quote = random.choice(quote_list)

if today == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # transport layer security
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="nishantguvvada0891@gmail.com", msg=f"Subject:Mail via SMTP\n\n{final_quote}")
else:
    print("Wait")