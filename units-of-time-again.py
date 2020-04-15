seconds = int(input("Enter number of seconds: "))

seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

days = seconds // seconds_in_day
seconds - seconds % seconds_in_day

hours = seconds // seconds_in_hour
seconds = seconds % seconds_in_hour

minutes = seconds // seconds_in_minute
seconds = seconds % seconds_in_minute

print("The equivalent duration is")
print("%d:%02d:%02d:%02d" % (days, hours, minutes, seconds)) 