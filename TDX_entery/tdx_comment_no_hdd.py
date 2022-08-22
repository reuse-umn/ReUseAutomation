# Prints "Received by ReUse [Current Date]. HDD N/A.
# Last updated 08/01/22.
import datetime

todays_date = datetime.date.today() # system.exec_command("date")
# Formatting date to get into mm/dd/yyyy format...
todays_date = datetime.date.strftime(todays_date, "%m/%d/%y")
keyboard.send_keys("Received by ReUse " + todays_date + ". HDD N/A.")
