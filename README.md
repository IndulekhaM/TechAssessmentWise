# 🚀 Automated Testing with Selenium WebDriver

## 📌 Overview
This project automates the testing of the **Wise Staging Environment** using **Selenium WebDriver** and **Python**. The script verifies key functionalities such as login, navigation to classrooms, session scheduling, and session validation.

## 🎯 Problem Statement
Automate a critical user flow on the **Wise** platform using Selenium:
- **Login as a Tutor** using phone number authentication.
- **Navigate to the Classroom** and verify successful access.
- **Schedule a Live Session** at 10 PM.
- **Validate Session Details** on the timeline.

## ⚙️ Tech Stack
- **Language**: Python 🐍
- **Framework**: Selenium WebDriver 🌐
- **Dependencies**: WebDriver Manager, Logging, PyTest

## 📂 Project Structure
```
├── main.py                # Main script containing test automation logic
├── requirements.txt       # Dependencies required to run the script
├── README.md              # Project documentation
```

## 🔥 Setup & Execution

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/wise-automation.git
cd wise-automation
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run Tests
```sh
pytest tests/
```

## 🧪 Test Scenarios
| #  | Test Case                     | Expected Outcome |
|----|--------------------------------|------------------|
| ✅ | **Login as Tutor**             | Institute name displayed |
| ✅ | **Navigate to Classroom**      | Classroom opens successfully |
| ✅ | **Schedule Live Session**      | Session is scheduled at 10 PM |
| ✅ | **Validate Session Details**   | Instructor, time, and status are correct |

## ⚠️ Troubleshooting
- **Session Card Not Found?** Ensure session creation was successful before validating.
- **Element Not Clickable?** Try adding `time.sleep(2)` before interaction (for debugging only).
- **WebDriver Issues?** Run `webdriver-manager` to update drivers.

## 📌 Future Enhancements
- ✅ Implement **headless mode** for CI/CD pipelines.
- ✅ Add **reporting & logging** for better test insights.
- ✅ Parameterize tests for **multiple environments**.

## 📧 Contact
For any issues or inquiries, feel free to reach out!




