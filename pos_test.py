import datetime
import json
import time
from clear_data import clear_data
from data_initialize import data_initialize
import pandas as pd
import os

from send_order import send_order

data_initialize('orders.ini', 'data.json')
with open('data.json') as f:
    data = json.load(f)

# Define output data
output = []

# Read the data.json file and pass the order_id, access_token, and image_path to the send_order function

def send_all_orders(data, output):
    access_token = data["access_token"]
    for order in data["orders"]:
        order_id = order["order_id"]
        image_path = order["image_path"]
        order_content_upload_status,order_send_message_response,order_output_link,error = send_order(order_id, access_token, image_path)
        if not any(order['order_id'] == order_id for order in output):
            output.append({
                "order_id": order_id,
                "content_upload_status": order_content_upload_status, 
                "send_message_response": order_send_message_response, 
                "output_link": order_output_link,
                "error": error
            })

send_all_orders(data, output)

# Assuming 'output' is your list of dictionaries
df = pd.DataFrame(output)

# Rename the columns
df.rename(columns={
    'order_id': 'Ma don hang',
    'content_upload_status': 'Trang thai up anh',
    'send_message_response': 'Trang thai gui tin nhan',
    'output_link': 'Link',
    'error': 'Loi'
}, inplace=True)

clear_data('data.json')

# Get current date and time
now = datetime.datetime.now()

# Format date and time as strings
date_str = now.strftime('%Y-%m-%d')
time_str = now.strftime('%H-%M-%S')

# Create directory if it doesn't exist
output_dir = os.path.join('outputs', date_str)
os.makedirs(output_dir, exist_ok=True)

# Save the DataFrame as an Excel file
output_file = os.path.join(output_dir, f'output_{time_str}.xlsx')
df.to_excel(output_file, index=False)

# Pause until user input
input("Press any key to exit...")