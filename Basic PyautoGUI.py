import time
import pyautogui

# Print the resolution of the screen
print(pyautogui.size())

# Move the mouse to coordinates (100, 100) over 5 seconds
pyautogui.moveTo(100, 100, duration=5)

# Print the current position of the mouse
print(pyautogui.position())

# Move the mouse relatively by 100 pixels horizontally and 100 pixels vertically over 10 seconds
pyautogui.moveRel(100, 100, duration=10)

# Click at the position (500, 500) three times with a 3-second interval between clicks
pyautogui.click(500, 500, clicks=3, interval=3, button="left")

# Triple click at the position (x, y) with a specified number of clicks and interval
pyautogui.tripleClick(x, y, clicks=3, interval=0.5)

# Double click at the position (x, y) with a specified number of clicks and interval
pyautogui.doubleClick(x, y, clicks=2, interval=0.5)

# Right click at the position (x, y) with a specified number of clicks and interval
pyautogui.rightClick(x, y, clicks=1, interval=0.5)

# Left click at the position (x, y) with a specified number of clicks and interval
pyautogui.leftClick(x, y, clicks=1, interval=0.5)

# Scroll up by 500 pixels
pyautogui.scroll(500)

# Scroll down by 500 pixels
pyautogui.scroll(-500)

# Perform a mouse up action at coordinates (100, 100)
pyautogui.mouseUp(100, 100, button='left')

# Perform a mouse down action at coordinates (100, 100)
pyautogui.mouseDown(100, 100, button='left')

# Type "hello" with keyboard input
pyautogui.write("hello")

# Press the "Enter" key
pyautogui.press("enter")

# Press the "Space" key
pyautogui.press("space")

# Display an alert with text 'virus' and title 'fake virus', with an 'OK' button
pyautogui.alert(text='virus', title='fake virus', button='OK')

# Prompt the user to enter their name
a = pyautogui.prompt(text='Enter name', title='Input box', default='')

# Print a greeting message with the entered name
print("Greetings " + a)

# Prompt for a password input (masked with '*')
pyautogui.password(text='Enter password', title='Password Prompt', mask='*')

# Display a confirmation box with custom buttons
pyautogui.confirm(text='Are you sure?', title='Confirmation', buttons=['OK', 'Cancel'])
