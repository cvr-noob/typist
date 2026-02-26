with open("code.txt", "r") as f:
    text = f.read()

from pynput.keyboard import Controller, Key
from time import sleep

c = Controller()

sleep(2)

c.press(Key.ctrl_l)
c.tap('a')
c.release(Key.ctrl_l)

for line in text.split('\n'):
    c.type(line)
    
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
