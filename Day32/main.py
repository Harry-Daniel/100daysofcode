import smtplib
import datetime as dt
import random


MY_EMAIL="testertont351@gmail.com"
MY_PASSWORD="adabrakadabra"


now=dt.datetime.now()
weekday=now.weekday()
if weekday == 5:
    with open("Day32/quotes.txt") as quote_file:
        all_quotes= quote_file.readlines()
        quote=random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Monday Motivation\n\n{quote}")