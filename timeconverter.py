#This program will convert time from one timezone to another.

from datetime import datetime
import pytz

print("Welcome to the time zone converter.\n")
user_time = input("Please enter the time in the format HH:MM AM/PM "
  "that you would like to convert\n")
user_timezone = input("Please enter what time zone the given time is in\n")
desired_timezone = input("Enter the time zone you want to convert to:\n")

# Convert user entered time to datetime object
user_datetime = datetime.strptime(user_time, "%I:%M %p")
user_timezone_obj = pytz.timezone(user_timezone)
user_datetime = user_timezone_obj.localize(user_datetime)

# Convert user datetime to desired timezone
desired_timezone_obj = pytz.timezone(desired_timezone)
desired_datetime = user_datetime.astimezone(desired_timezone_obj)

# Print the converted time
print("The converted time is:", desired_datetime.strftime("%I:%M %p"))