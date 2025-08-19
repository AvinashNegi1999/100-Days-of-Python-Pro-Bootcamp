# ============================================================
# BIRTHDAY EMAIL AUTOMATION PROGRAM
# ============================================================
# Author   : Avinash Negi
# Purpose  : Automatically send personalized "Happy Birthday"
#            emails to people whose birthdays match today’s date.
# Features :
#   ✅ Reads birthdays from a CSV file
#   ✅ Picks a random letter template
#   ✅ Personalizes the message with the recipient’s name
#   ✅ Sends the email using Outlook (SMTP)
#   ✅ Prints log messages (success / no birthdays)
# ============================================================


import datetime as dt
import pandas
import random
import smtplib
import os

# ✅ Gmail credentials (use app password, not normal login password)
MY_EMAIL = "avinashnegi1999temp@gmail.com"
MY_PASSWORD = "znrivdixpkrrnchi"

# ✅ Randomly choose one of the predefined birthday letter templates
random_num = random.randint(1, 3)
random_letter = f"letter_{random_num}.txt"

# ✅ Get today’s month and day (used to check birthdays)
now = dt.datetime.now()
month_day = (now.month, now.day)

# ✅ Load the birthday data from a CSV file
# * CSV columns must include: name, email, year, month, day
data = pandas.read_csv(
    r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 032\birthdays.csv"
)

# ✅ Convert DataFrame into dictionary
# * Key = (month, day)
# * Value = full row (person’s details)
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

# ✅ If today’s date matches a birthday → send an email
if month_day in birthdays_dict:
    birthday_person = birthdays_dict[month_day]

    # ✅ Build the full path to the chosen letter template
    base_dir = os.path.dirname(__file__)
    letter_path = os.path.join(base_dir, "letter_templates", random_letter)

    # ✅ Open the letter template and personalize it with the recipient’s name
    with open(letter_path, "r") as file:
        letter_data = file.read()
    letter_data = letter_data.replace("[NAME]", birthday_person["name"])

    # ✅ Connect to Gmail’s SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # ! Secure the connection
        connection.login(MY_EMAIL, MY_PASSWORD)  # ! Login using Gmail app password
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{letter_data}",
        )

    # ✅ Log a success message
    print(
        f"[INFO] Birthday email sent to {birthday_person['name']} ({birthday_person['email']})."
    )

else:
    # ✅ If no birthdays today, log a message instead
    print("[INFO] No birthdays today.")
