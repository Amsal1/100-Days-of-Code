import datetime as dt
import pandas as pd
import random
import smtplib

today = dt.datetime.now()
day = today.day
month = today.month
my_email = ""
password = ""
df = pd.read_csv("birthdays.csv")
for i in range(len(df)):
    if df['month'][i] == month and df['day'][i] == day:
        name = df['name'][i]
        email = df['email'][i]
        a = random.randint(1, 3)
        with open(f"./letter_templates/letter_{a}.txt") as letter:
            txt = letter.read()
            wish = txt.replace("[NAME]",f"{name}")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject: Happy Birthday to You!\n\n {wish}"
                )
