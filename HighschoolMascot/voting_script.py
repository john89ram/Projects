from selenium import webdriver
import time

# Specify the path to the Chrome WebDriver executable
# Replace 'path_to_chromedriver' with the path to your chromedriver executable
driver_path = 'path_to_chromedriver/chromedriver.exe'  # Update with your actual path

# Initialize Chrome WebDriver
driver = webdriver.Chrome(driver_path)

# Navigate to the website
driver.get('url_of_voting_website')

# Example: Replace 'Your High School' and 'Vote Button' with actual element locators
# Locate and interact with elements on the webpage
while True:
    try:
        school_element = driver.find_element_by_xpath("xpath_to_school_element")
        vote_button_element = driver.find_element_by_xpath("xpath_to_vote_button")

        school_element.click()
        vote_button_element.click()
        print("Voted successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Refresh the page and repeat after a delay
    driver.refresh()
    time.sleep(1)  # Adjust the delay as needed
