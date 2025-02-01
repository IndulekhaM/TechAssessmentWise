import time
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants (for easy modification)
BASE_URL = "https://staging-web.wise.live"
PHONE_NUMBER = "1111100000"
OTP = "0000"
SESSION_TIME = "10:00"
EXPECTED_INSTRUCTOR = "WISE TESTER"
EXPECTED_SESSION_NAME = "Live Session"


# Function to initialize WebDriver
def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

# Function to wait for an element and return it
def wait_for_element(driver, by, value, timeout=10, clickable=False):
    try:
        condition = EC.element_to_be_clickable((by, value)) if clickable else EC.presence_of_element_located((by, value))
        return WebDriverWait(driver, timeout).until(condition)
    except Exception as e:
        logging.error(f"Error finding element {value}: {e}")
        driver.quit()
        exit()


# Function to perform login
def login_and_assert_institute(driver):
    driver.get(BASE_URL)
    logging.info("Navigating to login page...")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/main/div/div/div/div/div/div/div/button[2]/span"))
    ).click()

    phone_input = wait_for_element(driver, By.TAG_NAME, "INPUT")
    phone_input.send_keys(PHONE_NUMBER)

    # Submit phone number and wait for OTP input
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div/div/div/div/div/div/div[2]/button/span").click()

    # Wait until OTP field appears
    otp_input = wait_for_element(driver, By.XPATH, "/html/body/div[1]/div/div/div/main/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/div/div/div/input", 10)
    otp_input.send_keys(OTP)
    otp_input.send_keys(Keys.RETURN)

    # Verify Institute Name
    institute_name = wait_for_element(driver, By.XPATH, "/html/body/div[1]/div/div/div/main/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div")
    assert institute_name.is_displayed(), "❌ Institute name is not displayed."
    logging.info("✅ Login successful and institute verified.")


# Function to navigate to classroom
def go_to_classroom(driver):
    logging.info("Navigating to Group Courses...")
    wait_for_element(driver, By.XPATH, "/html/body/div[1]/div/div/div/main/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]", clickable=True).click()

    logging.info("Cancel process to ADD a new course...")
    wait_for_element(driver, By.XPATH,"/html/body/div[1]/div/div/div[3]/div/div/div[2]/div[5]/div[1]/button/span",clickable=True).click()

    logging.info("Opening 'Classroom for Automated Testing'...")
    classroom = wait_for_element(driver, By.XPATH, "/html/body/div[1]/div/div/div[1]/main/div/div/div/div[1]/div/div[3]/div/div[1]/div/table/tbody/tr[1]/td[1]/div/div/a")

    # Validate classroom title
    assert classroom.is_displayed(), "❌ Classroom did not open successfully."
    logging.info("✅ Classroom opened successfully.")
    classroom.click()


# Function to schedule a session
def schedule_session(driver):
    logging.info("Navigating to Live Sessions tab...")
    wait_for_element(driver, By.XPATH, "//a[contains(text(), 'Live Sessions')]", clickable=True).click()

    schedule_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Schedule Sessions')]/ancestor::button"))
    )
    schedule_button.click()

    logging.info("Adding new session...")
    wait_for_element(driver, By.XPATH, "/html/body/div[1]/div/div/div[1]/main/div/div/div/div[1]/div[2]/div[1]/div/div[9]/div[1]/button/span", clickable=True).click()
    time.sleep(10)

    time_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//span[contains(text(), 'Create')]/ancestor::button"))
    )
    time_input.click()
    time_input.send_keys("10:00")

    logging.info("Creating session...")
    wait_for_element(driver, By.XPATH, "/html/body/div[1]/div/div/div[1]/main/div/div/div/div[1]/div[1]/div[2]/button", clickable=True).click()
    logging.info("✅ Session scheduled successfully.")

    logging.info("Opening 'Classroom for Automated Testing'...")
    classroom = wait_for_element(driver, By.XPATH,"//a[contains(text(), 'Classroom for Automated testing')]",timeout=10)
    classroom.click()

# Function to assert session details
def assert_session_details(driver):
    logging.info("Validating session details...")

    # Wait for session card to be visible
    sessions_card = wait_for_element(driver, By.XPATH, "/html/body/div[1]/div/div/div[1]/main/div/div/div/div[1]/div/div/div[3]/div[1]/div/div/div[3]/div/div[1]",timeout=20)

    # Ensure element is displayed before clicking
    if sessions_card.is_displayed():
        driver.execute_script("arguments[0].scrollIntoView();", sessions_card)  # Scroll to element
        time.sleep(10)  # Small delay before clicking
        sessions_card.click()
    else:
        logging.error("❌ Session card is not visible or interactable.")
        driver.quit()
        exit()

    instructor_name = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div/div[1]/div[3]/div[2]/div/div[1]/div[2]").text.strip()
    session_name = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div/div[1]/div[3]/div[2]/div/div[1]/div[1]/div/div").text.strip()
    session_time = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div/div[1]/div[3]/div[2]/div/div[1]/div[3]").text.strip()
    upcoming_status = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div/div[1]/div[3]/div[2]/div/div[1]/span/span").text.strip()

    assert instructor_name == EXPECTED_INSTRUCTOR, f"❌ Instructor name mismatch: {instructor_name}"
    assert session_name == EXPECTED_SESSION_NAME, f"❌ Session name mismatch: {session_name}"
    assert session_time == SESSION_TIME, f"❌ Session time mismatch: {session_time}"
    assert upcoming_status == "Upcoming", f"❌ Session status is incorrect: {upcoming_status}"

    logging.info("✅ Session details verified successfully.")


# Main Execution
if __name__ == "__main__":
    driver = setup_driver()

    try:
        login_and_assert_institute(driver)
        go_to_classroom(driver)
        schedule_session(driver)
        assert_session_details(driver)

    finally:
        time.sleep(5)  # Allow time to view results
        driver.quit()
        logging.info("Test execution completed. Browser closed.")
