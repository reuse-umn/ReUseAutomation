for i in range(28):
    keyboard.send_keys("<shift>+<tab>")

keyboard.send_keys("<shift>+<tab>")
keyboard.send_keys("<page_up>")
keyboard.send_keys("<tab>")

keyboard.wait_for_keypress("<tab>", modifiers=[], timeOut=30.0)
for i in range(5):
    keyboard.send_keys("<shift>+<tab>")
keyboard.wait_for_keypress("<tab>", modifiers=[], timeOut=30.0)
for i in range(4):
    keyboard.send_keys("<shift>+<tab>")