delay = 1

time.sleep(delay)
keyboard.send_keys("\t\t\t\t\t ")
keyboard.send_keys("\t\t10293")
time.sleep(delay*6)
keyboard.send_keys("\t\t\t\tahcware")
time.sleep(delay*5)
for i in range(15):
    keyboard.send_keys("\t")
    time.sleep(delay*.25)