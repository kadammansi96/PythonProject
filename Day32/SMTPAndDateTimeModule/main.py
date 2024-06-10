# import smtplib
#
# my_email = "mansitalhan@yahoo.com"
# password = "Tiktak@0312"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="mansitalhan@gmail.com", msg="Hello")


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1996, month=12, day=3)
print(date_of_birth)