from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL="testertont351@gmail.com"
MY_PASSWORD="abrakadabra"
# 2. Check if today matches a birthday in the birthdays.csv 
today=(datetime.now().month,datetime.now().day)

data=pandas.read_csv("Day32/birthday-wisher-hard-start/birthdays.csv")

birthday_dict={
    
}

birthday_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"Day32/birthday-wisher-hard-start/letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday!\n\n{contents}")




