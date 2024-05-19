# Automated WhatsApp Message Sender Documentation

## Overview

This script uses `pyautogui` and `webbrowser` modules to automate the process of sending messages on WhatsApp Web. The user inputs the contact's name or number, the message, and the number of times the message should be sent. The script then opens WhatsApp Web, searches for the contact, and sends the specified message the given number of times.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Script Explanation](#script-explanation)
4. [Running the Script](#running-the-script)
5. [Considerations](#considerations)
6. [Conclusion](#conclusion)

## Prerequisites

- Python 3.x installed on your system.
- The `pyautogui` library for GUI automation.
- A web browser installed (the script uses the default web browser).
- Internet connection to access WhatsApp Web.
- An active session of WhatsApp Web logged into your WhatsApp account.

## Installation

1. **Install `pyautogui`**:
   ```bash
   pip install pyautogui
   ```

2. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/BotirBakhtiyarov/WhatsAPP_send_message_bot.git
   cd whatsapp-automation
   ```

## Script Explanation

### Importing Libraries

```python
import webbrowser
import pyautogui as pt
import time
```

- `webbrowser`: Opens WhatsApp Web.
- `pyautogui`: Automates the keyboard and mouse actions.
- `time`: Manages delays in the script for proper synchronization.

### User Inputs

```python
reciver_contact = input("Enter Contact number or Name: ")
message = input("Enter your message: ")
limit = input("How many times: ")
```

- `reciver_contact`: Contact's name or number to search on WhatsApp.
- `message`: The message to be sent.
- `limit`: The number of times the message should be sent.

### Opening WhatsApp Web

```python
webbrowser.open("https://web.whatsapp.com/")
time.sleep(15)
```

- Opens WhatsApp Web in the default browser and waits 15 seconds for the user to scan the QR code if not already logged in.

### Searching for the Contact

```python
pt.click(120,170)
pt.typewrite(reciver_contact)
```

- Clicks on the search bar and types the contact's name or number.

### Selecting the Contact

```python
time.sleep(2)
pt.click(207,305)
```

- Waits for 2 seconds and clicks on the contact from the search results.

### Sending the Message

```python
i = 1
while i <= int(limit):
    time.sleep(1)
    pt.click(593,836)
    pt.typewrite(message)
    time.sleep(1)
    pt.click(1404,838)
    i += 1
```

- Enters a loop to send the message the specified number of times.
- Clicks on the message input field, types the message, and clicks the send button in each iteration.

## Running the Script

1. Ensure you have an active WhatsApp Web session in your default browser.
2. Run the script:
   ```bash
   python whatsapp_automation.py
   ```
3. Enter the required inputs when prompted:
   - Contact number or name.
   - Message to be sent.
   - Number of times to send the message.

## Considerations

- **Screen Resolution**: The script relies on specific coordinates for clicking. If your screen resolution or browser layout differs, you might need to adjust the coordinates.
- **Delay Time**: Adjust the `time.sleep()` values if your internet connection is slow or if the webpage takes longer to load.
- **Ethical Use**: Use this script responsibly. Avoid spamming contacts, as it may lead to your WhatsApp account being flagged or banned.

## Conclusion

This script provides an automated way to send repeated messages on WhatsApp Web using Python. It leverages `pyautogui` for GUI automation and `webbrowser` to open WhatsApp Web. Ensure to use the script ethically and adjust the coordinates and delay times as needed for your specific setup.
