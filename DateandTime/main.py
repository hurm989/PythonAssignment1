from datetime import date,datetime,timedelta
import pytz
# Write a Python program that uses the date module to print the current date in the format "YYYY-MM-DD".


# current_time=datetime.now()
# print(current_time)


# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

# my_date="09/12/2000"
# input_date_obj = datetime.strptime(my_date, "%m/%d/%Y")
# print(input_date_obj)

# Write a program that takes a birth year as input and calculates the age of a person.

# def birth_year(year):
#     current_year=datetime.now().year
#     myage=current_year-year
#     return myage
# age=birth_year(2000)
# print(age)



# Create a program that calculates and prints the number of days remaining until a person's next birthday.




# birthdate = datetime.strptime("2000-03-22", "%Y-%m-%d")
# current_date = datetime.now()
# next_birthday = datetime(current_date.year, birthdate.month, birthdate.day)

# if next_birthday < current_date:
#     next_birthday = next_birthday.replace(year=current_date.year + 1)
#     days_until = (next_birthday - current_date).days
#     print(days_until)

# Write a program that calculates and displays the number of days between two given dates.

# start_date_obj = datetime.strptime("22-03-2000", "%d-%m-%Y")
# end_date_obj = datetime.strptime("22-04-2000", "%d-%m-%Y")

# _between = (end_date_obj - start_date_obj).days
# print(_between)

# Create a program that takes a date as string and returns the corresponding day of the week (e.g., Monday, Tuesday, etc.).

# date_obj = datetime.strptime("22-03-2000", "%d-%m-%Y")
        
# day_of_week = date_obj.strftime("%A")
        
# print(day_of_week)


# Create a program that takes a year and a month as input and prints the number of days in that month.
# without using calender module

# Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.

# start_date = datetime.strptime( "2022-12-25", "%Y-%m-%d")
# future_date = start_date + timedelta(days=2)
# future_date_str = future_date.strftime("%Y-%m-%d")
# print(future_date_str)

# Write a Python program that uses the datetime module to print the current date and time.

# current_datetime = datetime.now()
# formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_datetime)

# Create a function that takes a datetime in the format "MM/DD/YYYY HH:MM:SS" as string  formats it as "YYYY-MM-DD HH:MM:SS".

# input_datetime = datetime.strptime("03/22/2000 00:00:00", "%m/%d/%Y %H:%M:%S")
# formatted_datetime_str = input_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_datetime_str)


# Write a program that calculates the time difference between two given datetime objects and displays it in hours, minutes, and seconds.
# datetime1 = datetime.strptime("2000-03-22 00:00:00", "%Y-%m-%d %H:%M:%S")
# datetime2 = datetime.strptime("2001-03-22 00:00:00", "%Y-%m-%d %H:%M:%S")
# time_difference = datetime2 - datetime1
# hours, remainder = divmod(time_difference.total_seconds(), 3600)
# minutes, seconds = divmod(remainder, 60)
# print(minutes,seconds,hours)


# Write a program that takes a date string in the format "MM-DD-YYYY" as input and converts it to a datetime object using strptime().

# Create a function that takes a datetime object as input and formats it as "Month Day, Year" (e.g., "August 25, 2023") using strftime().

# Create a function that takes a datetime object as input and formats it as "Day-Month-Year" (e.g., "25-August-2023") using strftime().

# create a datetime object from the string "26-08-2023 15:18:33.983780-07:00" 
# hint: https://strftime.org/

# create a datetime object from the string "08-26-2023 08:10:00 PM"
# hint: https://strftime.org/

# create a datetime object from the string "08-26-2023 08:10:00 PM"
# hint: https://strftime.org/

# dt_named_and_short_form_format = "8-August-23 08:10:00"
# hint: https://strftime.org/


# create a current datetime and then displays it in the format "HH:MM AM/PM"

# Write a program that takes a user-entered date in the format "MM/DD/YYYY" and prints it in the format "YYYY-MM-DD".

# Create a function that takes a datetime object as input and displays the day of the week (e.g., "Monday") using strftime().
# hint: https://strftime.org/
# datetime_obj = datetime.strptime("2023-09-16 08:30:00", "%Y-%m-%d %H:%M:%S")
# day_of_week = datetime_obj.strftime("%A")
# print(day_of_week)

# Create a function that takes a timezone name as input and prints the current date time object in that timezone.


# tz = pytz.timezone("America/New_York")
# current_time = datetime.now(tz)
# print(f"Current datetime in {tz}: {current_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# Write a program that converts a given date time (tz aware) string from one timezone to another.
# from_tz = pytz.timezone("America/New_York")
# to_tz = pytz.timezone("Europe/London")

# dt = datetime.strptime("2023-09-16 12:00:00 America/New_York", "%Y-%m-%d %H:%M:%S %Z")
# dt = from_tz.localize(dt)

# converted_dt = dt.astimezone(to_tz)

# converted_datetime_str = converted_dt.strftime("%Y-%m-%d %H:%M:%S %Z")

# print( converted_datetime_str)

# Write a program that takes a datetime object (naive) and a timezone name as input, and returns a localized datetime object in the specified timezone.


# Create a function that takes a timezone name and a number of hours as input, and prints the current time plus the specified hours in that timezone

# tz = pytz.timezone("America/New_York")
# current_time_tz = datetime.now(tz)
# future_time_after_adding_hrs = current_time_tz + timedelta(hours=3)
# print(future_time_after_adding_hrs)


# Write a program that calculates the date and time of the daylight saving start in the year 2022.
# take timezone "US/Pacific"
# take string date as "2022-01-01 00:00:00"
# hint: use
# bool(tz_aware_dt.dst()) == True # dst activated
# bool(tz_aware_dt.dst()) == False # dst not activated


# Write a program that calculates the date and time of the daylight saving end in the year 2022.
# take timezone "US/Pacific"
# take string date as "2022-01-01 00:00:00"
# hint: use
# bool(tz_aware_dt.dst()) == True # dst activated
# bool(tz_aware_dt.dst()) == False # dst not activated

# Design a program that helps schedule a meeting across different timezones. The program should take the meeting time in one timezone and display the corresponding times in other timezones.
# consider three countries: UK, US, Saudi Arab and Pakistan
# consider the meeting time is: 30 August 2023 at 2 PM Pakistan time


# item System
# Design a item system where users specify a start datetime, end datetime, and timezone. Implement a function that checks whether a specified time slot is available.
# if timeslot is available then store the start_date and end_date in the list of objects i.e
"""
item_storage = [
  {
    "start_date": "",
    "end_date": ""
  }
]
"""
# hint 1: store dates in item_storage in UTC format i.e pytz.utc
# hint 2: use for loop, the loop should run 5 times. ask user input inside the loop

# instruction to test your program:
# first iteration of loop
# give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone

# second iteration of loop
# give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00" as end_date and "Asia/Riyadh" as timezone
# above program should not accept this item as the slot is already booked by the first iteration


# import pytz
# from datetime import datetime

# item_storage = []

# def is_slot_available(start_date, end_date):
#     for item in item_storage:
#         if start_date >= item["start_date"] and start_date < item["end_date"]:
#             return False
#     return True

# # Main loop to accept user input and check availability
# for _ in range(5):
#     start_date_str = input("Enter the start datetime (YYYY-MM-DD HH:MM:SS): ")
#     end_date_str = input("Enter the end datetime (YYYY-MM-DD HH:MM:SS): ")
#     timezone_str = input("Enter the timezone (e.g., 'Asia/Karachi'): ")

#     try:
#         # Parse input strings into datetime objects and set the timezone
#         start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
#         end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
#         timezone = pytz.timezone(timezone_str)

#         # Convert datetime objects to UTC timezone
#         start_date_utc = timezone.localize(start_date).astimezone(pytz.utc)
#         end_date_utc = timezone.localize(end_date).astimezone(pytz.utc)

#         # Check if the slot is available
#         if is_slot_available(start_date_utc, end_date_utc):
#             # If available, add to item_storage
#             item_storage.append({"start_date": start_date_utc, "end_date": end_date_utc})
#             print("item confirmed.")
#         else:
#             print("item slot is not available.")
#     except ValueError:
#         print("Invalid input format. Please use 'YYYY-MM-DD HH:MM:SS' for datetime.")

# print(item_storage)
# # for item in item_storage:
# #     print(f"Start: {item['start_date']} - End: {item['end_date']}")
