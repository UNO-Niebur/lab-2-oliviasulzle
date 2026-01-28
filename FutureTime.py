#FutureTime.py
#Name: Olivia Sulzle
#Date: 2/1/26
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute


  #TODO:
  #Ask user for hours
  hours_to_add = int(input("Enter hours to add: "))
  #Ask user for minutes
  minutes_to_add = int(input("Enter minutes to add: "))

  #Calculate the time after the user-supplied time has passed.
  total_minutes = currentMinute + minutes_to_add
  final_minute = total_minutes % 60
  extra_hour = total_minutes // 60

  total_hours = currentHour + hours_to_add + extra_hour
  final_hour = total_hours % 24

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print(f"Future time: {final_hour:02}:{final_minute:02}")


if __name__ == '__main__':
  main()
