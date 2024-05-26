from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import os
import json

input_file = 'orders.ini'
data_file = 'data.json'

def data_initialize(input_file,data_file):
    with open('data.json') as f:
        data = json.load(f)
    if not os.path.exists('images'):
        os.makedirs('images')

    # Initialize an empty list
    orders_array = []

    # Open the file and read the lines
    with open(input_file, 'r') as f:
        orders_array = [line.strip() for line in f]

    print(orders_array)


    # Setup Selenium
    options = Options()
    options.headless = True

    # Create the driver
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # URL to access
    login_url = 'https://app.anousith-express.com/login' 
    driver.get(login_url)

    # Login
    username_field = driver.find_element(By.NAME,"username")  
    password_field = driver.find_element(By.NAME,"password")  
    username_field.send_keys(data['anousith_username']) 
    password_field.send_keys(data['anousith_password'])  

    button = driver.find_element(By.CSS_SELECTOR,"button.btn.btn-danger.btn-block.btn-lg.mb-1.mt-1.btn-radius")
    button.click()
    time.sleep(2.5)


    for order_id in orders_array:
        image_path = os.path.join('images', order_id+'.png')

        # Check if the image already exists
        if not os.path.isfile(image_path):
            homepage_url = 'https://app.anousith-express.com/nextday/home'

            # Access the URL
            driver.get(homepage_url)

            bill_input_field = driver.find_element(By.CSS_SELECTOR,"body > div.row.p-2 > div.col-md-12.col-lg-10.m-auto.justify-content-md-center.mt-5 > div > div > div > input")
            bill_input_field.send_keys(order_id)
            bill_search_button = driver.find_element(By.CSS_SELECTOR,"body > div.row.p-2 > div.col-md-12.col-lg-10.m-auto.justify-content-md-center.mt-5 > div > div > button")
            bill_search_button.click()
            time.sleep(0.5)
            bill = driver.find_element(By.CSS_SELECTOR,"#root > div > div > div > div > div.section.full.mb-1.mt-1 > div.bill-content")

            with open(image_path, 'wb') as file:
                file.write(bill.screenshot_as_png)

        # Update the JSON data
        # Check if the order_id already exists in the 'orders' list
        if not any(order['order_id'] == order_id for order in data['orders']):
            # If not, append the new order
            data['orders'].append({"image_path": image_path, "order_id": order_id})

    # Write the updated data back to the JSON file
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    # Close the driver
    driver.quit()


# Search for bill by ID Plan B

# bill_id = '8222445075555'
# start_date = '2024-05-10'
# end_date = '2024-05-10'

# for i in range(1, 100):
#     url = 'https://app.anousith-express.com/nextday/history/list_bill?tab=other_history&get_click=sent_to&search=' + bill_id + '&startDate=' + start_date + '&endDate=' + end_date + '&page='+str(i)
#     driver.get(url)
#     time.sleep(1.5)
#     try:
#         bill_view = driver.find_element(By.CSS_SELECTOR,"#appCapsule > div.col-md-12.col-lg-8.m-auto.p-2 > div.customerHeaderLists > div > table > tr > div.customFont.customTopWeb.customTopDate")
#     except NoSuchElementException:
#         continue
#     else:
#         bill_view.click()
#         bill_zone = driver.find_element(By.CSS_SELECTOR,"body > div.modal.show > div > div")
#         time.sleep(5)
#         # Capture the webpage as a picture
#         with open('bill.png', 'wb') as file:
#             file.write(bill_zone.screenshot_as_png)
#         break
