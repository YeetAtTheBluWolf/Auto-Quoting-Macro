"""This is sample code used to get a position of the mouse on a screen."""

import pyautogui

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        POS = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(POS, end='')
        print('\b' * len(POS), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
