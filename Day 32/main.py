import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open("quotes.txt", "r") as file:
        lines = file.readlines()
    quote_of_the_day = random.choice(lines)
    my_email = "ak47.repacker@gmail.com"
    password = "kaneezsabri123"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ak47.oreo@gmail.com",
            msg=f"Subject: Monday Quote\n\n {quote_of_the_day}"
        )
