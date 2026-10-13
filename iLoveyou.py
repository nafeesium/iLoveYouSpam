import time

import pyautogui # type: ignore

MESSAGE = "I love you"
TIMES = 100
START_DELAY = 10
LETTER_DELAY = 0.01
PAUSE_AFTER_SEND = 0.3

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0

print(f"{START_DELAY}")

for left in range(START_DELAY, 0, -1):
    print(left, end=" ", flush=True)
    time.sleep(1)
print()

for n in range(1, TIMES + 1):
    for letter in MESSAGE:
        pyautogui.write(letter)
        time.sleep(LETTER_DELAY)
    pyautogui.press("enter")
    print(f"sent {n}/{TIMES}")
    time.sleep(PAUSE_AFTER_SEND)

print("Done.")
