# Prints "Received by ReUse [Current Date]. HDD (SN: " then waits for the serial number to be scanned before filling in with ") removed and sent to Dynamics."
# Last updated 08/01/22.
import datetime

todays_date = datetime.date.today() # system.exec_command("date")
# Formatting date to get into mm/dd/yyyy format...
todays_date = datetime.date.strftime(todays_date, "%m/%d/%y")
keyboard.send_keys("Received by ReUse " + todays_date + ". HDD (SN: ")
keyboard.wait_for_keypress("<enter>", modifiers=[], timeOut=10.0)
keyboard.send_keys("<backspace>) removed and sent to Dynamics.")