# AutoAttendanceBot

**AutoAttendanceBot** is an automation tool designed to streamline the process of marking attendance on web-based platforms. It automates the login process and attendance registration using Selenium WebDriver.

## Features
- Automated login to the attendance system
- Clicks the attendance button to mark presence
- Scheduled execution to mark attendance at regular intervals
- Robust error handling and logging

## Requirements
- Python 3.x
- [Selenium WebDriver](https://www.selenium.dev/documentation/en/webdriver/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)

## Installation

1. **Clone the repository** (if applicable):
    ```sh
    git clone https://github.com/yourusername/AutoAttendanceBot.git
    cd AutoAttendanceBot
    ```

2. **Install the required Python libraries**:
    ```sh
    pip install selenium pyautogui opencv-python numpy
    ```

3. **Download and set up the WebDriver**:
    - Download [ChromeDriver](https://sites.google.com/chromium.org/driver/) (for Chrome) or the appropriate WebDriver for your browser.
    - Ensure the WebDriver is in your system’s PATH or specify its location in the script.

## Configuration

1. **Edit the script to include your credentials**:
    - Open the `script.py` file and replace the placeholders with your login credentials:
    ```python
    username = ""  # Your login here
    password = ""  # Your password here
    ```

2. **Set the URL of the attendance portal**:
    - Update the `url` variable in the script to point to your attendance portal.

## Usage

1. **Run the script**:
    ```sh
    python script.py
    ```
    - The script will log in to the attendance system, click the attendance button, and repeat the process at the specified intervals.

2. **Stop the script**:
    - You can stop the script at any time using `Ctrl + C` in your terminal or command prompt.

## Troubleshooting
- **Login Issues**: Ensure your credentials are correct and the login elements on the page have not changed.
- **Button Not Found**: Verify that the XPath or CSS selectors used to locate the attendance button are accurate.
- **WebDriver Errors**: Make sure the WebDriver version matches your browser version and is properly installed.

