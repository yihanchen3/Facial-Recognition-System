
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Generate random username
def generate_username():
    return ''.join(random.choices(string.ascii_lowercase, k=6))

# Generate random password
def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

# Generate random email address
def generate_email():
    return f"{generate_username()}@example.com"

repeat = 5

# Loop for repeat number of times
for j in range(repeat):
    # Initialize browser driver
    driver = webdriver.Firefox()

    # Navigate to the signup page
    driver.get("http://127.0.0.1:8000/signup/")

    # Generate random username, email, and password
    username = generate_username()
    email = generate_email()
    password = generate_password()

    # Fill out the form with random username, email, and password
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys(username)

    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(email)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    # Click on the Start Camera button
    start_button = driver.find_element(By.ID, "startButton")
    start_button.click()

    # Wait for the camera to load
    wait = WebDriverWait(driver, 10)
    capture_button = wait.until(EC.presence_of_element_located((By.ID, "captureButton")))

    # Click the Capture Face button five times
    for i in range(5):
        capture_button.click()

    # Click on the Signup button
    signup_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    signup_button.click()

    # Print the generated username, email, and password
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Password: {password}")

    # Close the browser
    driver.quit()
