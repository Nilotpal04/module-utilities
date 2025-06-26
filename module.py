#Module
import random
from calendar import month, weekday


#OTP generator
def generate_otp():
    otp = random.randint(100000, 999999)
    return otp
print(generate_otp())

#Date logger
import datetime
now = datetime.datetime.now()

day = now.day
month = now.strftime("%B")
year = now.year
weekday = now.strftime("%A")
time = now.strftime("%H:%M:%S")

print(f"Today is: {day} {month} {year} {weekday}")
print(f"Time now: {time}")

#Square root calculator
import math
def sqr_root(x):
    num = math.sqrt(x)
    rounded_num = round(num, 2)
    return rounded_num
