import time
import pyperclip
from pynput import keyboard

def on_press(key):
    try:
        if key == keyboard.Key.f2:
            clipboard = pyperclip.paste()
            for char in clipboard:
                keyboard.Controller().type(char)
                time.sleep(0.05)
    except AttributeError:
        pass

# Listen for F2 key press
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()