for i in range(28):
    keyboard.send_keys("<shift>+<tab>")
keyboard.wait_for_keypress("<enter>", modifiers=[], timeOut=30.0)
for i in range(7):
    keyboard.send_keys("<shift>+<tab>")
keyboard.wait_for_keypress("<enter>", modifiers=[], timeOut=30.0)
for i in range(3):
    keyboard.send_keys("<shift>+<tab>")