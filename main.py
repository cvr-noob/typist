with open("code.txt", "r") as f:
    text = f.read()

from pynput.keyboard import Controller, Key
from time import sleep

c = Controller()

sleep(2)

c.press(Key.ctrl_l)
c.tap('a')
c.release(Key.ctrl_l)

# List of characters that Monaco typically auto-closes
auto_close_chars = ['(', '[', '{', '"', "'"]

for line in text.split('\n'):
    for char in line:
        c.type(char)
        
        # If the character triggers an auto-completed pair, delete the pair immediately
        if char in auto_close_chars:
            # Tiny sleep to ensure Monaco has time to render the auto-completed character
            sleep(0.02) 
            # 'Delete' removes the character immediately to the right of the cursor
            c.tap(Key.delete) 
            
    c.tap(Key.enter)

    sleep(0.05)
    c.tap(Key.home)

c.press(Key.shift_l)
c.tap(Key.end)
c.release(Key.shift_l)
c.tap(Key.delete)

c.press(Key.ctrl_l)
c.tap("'")
c.release(Key.ctrl_l)
