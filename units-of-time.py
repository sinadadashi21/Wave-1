days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

total_seconds = days * seconds_in_day + hours * seconds_in_hour + minutes * seconds_in_minute + seconds
print("The total number of seconds represented by this duration is:", total_seconds)