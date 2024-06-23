from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
from PIL import ImageGrab
import dotenv
import os

dotenv.load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

def get_mind_map(text):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')
    
    # Setup WebDriver with options
    driver = webdriver.Chrome(options=options)
    driver.get("https://whimsical.com/")
    time.sleep(5)
    
    # Click login button
    login_button = driver.find_element(By.CLASS_NAME, 'styles_login__M_XWz')
    login_button.click()
    time.sleep(5)
    
    # Enter login details
    driver.find_element(By.CLASS_NAME, 'email').send_keys(EMAIL)
    driver.find_element(By.CLASS_NAME, 'password').send_keys(PASSWORD)
    driver.find_element(By.CLASS_NAME, 'submit').click()
    time.sleep(5)

    # Click the element using JavaScript to avoid interception
    element = driver.find_element(By.CSS_SELECTOR, '[data-tooltip-id="G__189"]')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(5)
    
    # Click 'New Board' button using JavaScript
    new_board_button = driver.find_element(By.ID, 'new-file-board')
    driver.execute_script("arguments[0].click();", new_board_button)
    time.sleep(4)
    
    
    # Click 'Generate with AI' button
    generate_button = driver.find_element(By.ID, 'generate-with-ai-tool')
    driver.execute_script("arguments[0].click();", generate_button)
    time.sleep(2)
     
    #ph11
    driver.find_element(By.CLASS_NAME, 'ph11').send_keys(text)
    time.sleep(20)
    
    flow_Chart = driver.find_element(By.CSS_SELECTOR, '[data-tooltip-id="G__357"]')
    driver.execute_script("arguments[0].click();", flow_Chart)
    time.sleep(1)
    
    create_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Create (Control Enter)"]')
    create_button.click()
    time.sleep(20)
    
    # Simulate the shortcut 'Ctrl + Shift + C' to copy the flowchart as an image
    pyautogui.hotkey('ctrl', 'shift', 'c')
    time.sleep(3)
    
    # Capture the clipboard content
    image_path = ImageGrab.grabclipboard()
    
    # Save the image if it is not None
    if isinstance(image_path, ImageGrab.Image.Image):
        image_path.save('flowchart.png')
    else:
        print("No image found in clipboard.")
    
    # Quit the browser
    driver.quit()
    
    return 'flowchart.png'

if __name__ == '__main__':
    text = 'The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.'
    get_mind_map(text)
