# iLoveyou.py

A tiny Python script that types a message into whatever text box you have focused, presses Enter, and repeats. I made it to send "I love you" to my wife over and over, letter by letter, like I was typing it myself.

It waits 10 seconds when you start it, so you have time to switch to the app and click the message bar.

## What it does

1. Counts down 10 seconds.
2. Types the message one letter at a time.
3. Presses Enter.
4. Repeats 100 times.

It works with any app that has a text box.

## Requirements

- Python 3
- [pyautogui](https://pypi.org/project/PyAutoGUI/)

```
pip install pyautogui
```

If `pip` isn't recognized on Windows, use this instead:

```
python -m pip install pyautogui
```

## How to use

1. Run the script:

   ```
   python iLoveyou.py
   ```

2. During the countdown, click inside the message box.
3. Take your hands off the keyboard and mouse. It types into whatever window is focused.

## Stopping it

Move the mouse into any corner of the screen. pyautogui's fail-safe is turned on, so the script stops right away.

You can also press `Ctrl + C` in the terminal.

## Settings

Everything you might want to change is at the top of `iLoveyou.py`:

| Setting | Default | What it does |
| --- | --- | --- |
| `MESSAGE` | `"I love you"` | The text that gets typed |
| `TIMES` | `100` | How many times it is sent |
| `START_DELAY` | `10` | Seconds to wait before typing starts |
| `LETTER_DELAY` | `0.01` | Seconds between each letter |
| `PAUSE_AFTER_SEND` | `0.3` | Seconds to wait after each Enter |

If letters get dropped or messages get cut in half, raise `LETTER_DELAY` a little.

## Troubleshooting

**`ModuleNotFoundError: No module named 'pyautogui'`**
You probably have more than one Python installed, and the library went into a different one than the one running the script. Install it with the same interpreter that runs the file:

```
python -m pip install pyautogui
python iLoveyou.py
```

In VS Code, press `Ctrl + Shift + P`, choose **Python: Select Interpreter**, and pick the one you installed pyautogui into.

**Nothing gets typed**
Make sure the text box is focused before the countdown ends. On macOS, give your terminal permission under System Settings, then Privacy & Security, then Accessibility.

**It types into the wrong window**
The script has no idea where it is typing. It sends keys to whatever window is in front. Click the right box before the countdown ends.

## A note

Be kind with it. A hundred messages is sweet once, but check that the person on the other end is happy to get them. Lower `TIMES` if you're not sure.

## License

MIT. Do whatever you like with it.
