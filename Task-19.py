# Visit the URL https://www.saucedemo.com/ and login with the following credentials :-
# Username : standard_user Password : standard_user
# Try to fetch the following using Python Selenium :-
# 1.) Title of the webpage
# 2.) Current URL of the webpage
# 3. Extract the entire contents of the webpage and save it in. a Text file whose name will be "Webpage _task_11.txt"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

driver.get("https://www.saucedemo.com/")

Title_webpage = driver.title
print("Title of the webpage: ", Title_webpage)

url = driver.current_url
print("Current URL of the webpage:", url)


def extract_content():
    webpage_content = driver.find_element(By.TAG_NAME, "html").text
    print(webpage_content)

    f = open("Webpage _task_11.txt", "w")
    f.write(webpage_content)
    f.close()


extract_content()

driver.quit()