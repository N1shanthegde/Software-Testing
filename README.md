# Software Testing Automation Scripts

This repository contains Python automation scripts using Selenium WebDriver for testing web-based campus and parent portals.

## Contents

- **campusunoTestCase.py**  
  Automates login, navigation, notes download, fee payment, attendance checking, proctor system viewing, and logout on [campus.uno/sjbit](https://campus.uno/sjbit).

- **GAT_Website.py**  
  Automates login, navigation, attendance viewing, CIE results, events, timetable, previous performance, and logout on [globalparents.contineo.in](https://globalparents.contineo.in/newparentseven/index.php).

## Prerequisites

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- Chrome browser
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (ensure `chromedriver.exe` is in the project directory)

Install dependencies:
## Usage

1. **Update Credentials:**  
   Edit the scripts to enter your username, password, and other required fields.

2. **Run the Script:**
   
3. The script will launch Chrome, perform automated actions, and close the browser upon completion.

## Notes

- The scripts use hardcoded XPaths and time delays (`time.sleep`). Adjust these as needed for reliability.
- For other browsers, update the WebDriver initialization accordingly.
- Do not share your credentials.

## License

This project is for educational and testing purposes only.
