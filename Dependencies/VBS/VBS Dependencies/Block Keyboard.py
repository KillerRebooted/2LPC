import keyboard
import mouse
import time

#Block or Unblock Keyboard
def block_keyboard(bool):
    if bool:
        for i in range(150):
            keyboard.block_key(i)
    else:
        for i in range(150):
            keyboard.unblock_key(i)

#block_keyboard(True)

while True:
    time.sleep(5)