import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_wikipedia_search_results(search_term):
    # Path to Chrome WebDriver executable
    chrome_driver_path = "./chromedriver"

    # Create ChromeOptions object
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
    chrome_options.set_capability("pageLoadStrategy", "eager")
    chrome_options.add_argument("--window-size=1920x1080")

    # Set the path to the ChromeDriver executable
    chrome_service = ChromeService(chrome_driver_path)

    # Pass ChromeOptions to the webdriver when initializing
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Maximize the browser window to fullscreen (Not applicable in headless mode)
    driver.maximize_window()

    try:
        # Open Wikipedia
        driver.get("https://en.wikipedia.org/wiki/Main_Page")

        # Wait for the search input to be visible and enabled
        wait = WebDriverWait(driver, 10)
        search = wait.until(EC.element_to_be_clickable((By.NAME, 'search')))
        
        search.send_keys(search_term)
        search.submit()
        time.sleep(5)
        search_results_url = driver.current_url
        
        return search_results_url

    except Exception as e:
        print("Error occurred:", e)

    finally:
        # Close the browser
        driver.quit()

# Call the function with the search term 
search_term = 'modi'
result_url = get_wikipedia_search_results(search_term)
print("Search Results URL:", result_url)
