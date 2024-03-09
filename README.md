# PyAutoGUI Basics

This Python script demonstrates the usage of the PyAutoGUI library for automating mouse and keyboard actions, as well as handling alerts and prompts.

## Prerequisites

- Python 3.x installed on your system.
- Install the PyAutoGUI library using pip:
  ```bash
  pip install pyautogui
## Functionality

- **Mouse Actions:**
  - Moving the mouse to specific coordinates.
  - Clicking at specific coordinates with customizable parameters.
  - Scrolling the mouse up or down.
  - Performing mouse up and mouse down actions.

- **Keyboard Actions:**
  - Typing text.
  - Pressing keys like Enter and Space.

- **Alerts and Prompts:**
  - Displaying alerts with custom text and buttons.
  - Prompting the user to enter text or a password.
  - Confirming actions with custom buttons.

## Note

- Make sure to adjust the coordinates `(x, y)` in the script according to your screen resolution and the application window you're interacting with.

- Some functions like `tripleClick`, `doubleClick`, `rightClick`, and `leftClick` are not part of the `pyautogui` library. You can achieve similar functionality using the `click` function with appropriate parameters.

- This script is for educational purposes and should be used responsibly. Ensure you understand its functionality before running it, as it can automate tasks on your system.
