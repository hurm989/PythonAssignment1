# Booking System
# Design a booking system where users specify a start datetime, end datetime, and timezone. Implement a function that checks whether a specified time slot is available.
# if timeslot is available then store the start_date and end_date in the list of objects i.e
"""
booking_storage = [
  {
    "car_model": "", # corolla, civic

    "start_date": "",
    "end_date": ""
  }
]
"""
# hint 1: store dates in booking_storage in UTC format i.e pytz.utc
# hint 2: use for loop, the loop should run 5 times. ask user input inside the loop

# instruction to test your program:
# first iteration of loop
# give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone and car_model 

# second iteration of loop
# give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00" as end_date and "Asia/Riyadh" as timezone  and car_model 
# above program should not accept this booking as the slot is already booked by the first iteration

# You must write the following functions

# add_tz() # this should convert naive date to tz_awre
# convert_tz() # this should convert date from one tz to another
# is_slot_available() # this should return True or False
# book_the_car() # this should add the detail in booking_storage


from datetime import datetime,date 

import pytz

item_storage = []

def is_slot_available(start_date, end_date):
    for item in item_storage:
        if start_date >= item["start_date"] and start_date < item["end_date"]:
            return False
    return True
def  book_the_car(start_date_utc,end_date_utc):
        if is_slot_available(start_date_utc, end_date_utc):
            # If available, add to item_storage
            item_storage.append({"start_date": start_date_utc, "end_date": end_date_utc})
            print("item confirmed.")
        else:
            print("item slot is not available.")

def add_tz(timezone_str,start_date,end_date):
    timezone = pytz.timezone(timezone_str)
    start_date_utc = timezone.localize(start_date).astimezone(pytz.utc)
    end_date_utc = timezone.localize(end_date).astimezone(pytz.utc)
    return end_date_utc,start_date_utc
def convert_tz(start_date,end_date):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
    return start_date,end_date

for _ in range(5):
    start_date_str = input("Enter the start datetime (YYYY-MM-DD HH:MM:SS): ")
    end_date_str = input("Enter the end datetime (YYYY-MM-DD HH:MM:SS): ")
    timezone_str = input("Enter the timezone (e.g., 'Asia/Karachi'): ")

    try:
        
        start_date,end_date=convert_tz(start_date,end_date)
        start_date_utc,end_date_utc=add_tz(timezone_str)
        book_the_car(start_date_utc,end_date_utc)
    except ValueError:
        print("Invalid input format. Please use 'YYYY-MM-DD HH:MM:SS' for datetime.")

# Start Datetime: 2023-08-26 18:00:00
# End Datetime: 2023-08-26 19:00:00
# Timezone: Asia/Karachi