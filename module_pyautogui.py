import pyautogui

# Move the mouse to a specific location (x=100, y=100)
pyautogui.moveTo(100, 100)

# Click the mouse at its current location
pyautogui.click()

# Type a string at the current keyboard focus
pyautogui.write('Hello, world!')

# Press a single key
pyautogui.press('esc')