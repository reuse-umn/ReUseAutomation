import time
import threading
from pynput.keyboard import Key, Controller, Listener


def clicker():
    keyboard = Controller()

    while(True):
        for _ in range(5):
            keyboard.press(Key.f12)
            keyboard.release(Key.f12)
            time.sleep(2)

        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release(Key.ctrl)
        keyboard.release('w')
        time.sleep(2)
        if stop:
            break


def on_press(key):
    """Press F8 to start and stop autoclicker, press esc to stop script"""
    global thread
    global stop

    if thread is None:
        if key == Key.f8:
            stop = False
            print('Starting Clicker')
            thread = threading.Thread(target=clicker)
            thread.start()
    else:
        if key == Key.f8:
            stop = True
            print('Stopping')
            thread.join()
            del thread
            thread = None
    
    if key == Key.esc:
        listener.stop()
        print('Listener stopped')
    

if __name__ == '__main__':

    thread = None
    stop = False

    with Listener(on_press=on_press) as listener:
        listener.join()