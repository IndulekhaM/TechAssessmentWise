# Automated Testing with Selenium WebDriver

## 📌 Overview
This project is a Selenium WebDriver-based automation script designed to test the scheduling and validation of live sessions on the **WISE** platform. The script automates login, navigation, session scheduling, and validation steps.

## 🚀 Features
- Automated login with OTP authentication (mocked for testing purposes).
- Navigation to the classroom and scheduling a live session.
- Validation of session details including instructor name, session title, time, and status.
- Exception handling and logging for debugging.

## 🛠️ Tech Stack
- **Python** (Scripting Language)
- **Selenium WebDriver** (Automation Framework)
- **ChromeDriver** (WebDriver for Chrome)
- **WebDriver Manager** (For handling WebDriver binaries)
- **Logging** (For test tracking and debugging)

## 📂 Project Structure
```
├── main.py                # Main script containing test automation logic
├── requirements.txt       # Dependencies required to run the script
├── README.md              # Project documentation
```

## 📥 Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Google Chrome Browser

### Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running the Script
```bash
python main.py
```

## 🔎 Test Flow
1. **Login to the WISE platform**
   - Enters phone number and OTP (mocked for testing).
   - Asserts institute name visibility.
2. **Navigate to Group Courses**
   - Access the classroom section.
3. **Schedule a Live Session**
   - Opens scheduling panel and sets session details.
4. **Validate Session Details**
   - Checks instructor name, session title, and scheduled time.

## 🐞 Troubleshooting
- If the script fails to find an element, ensure:
  - The website layout hasn't changed.
  - Your network connection is stable.
  - ChromeDriver version is compatible with the installed Chrome browser.

## 📧 Contact
For any issues or inquiries, feel free to reach out!

