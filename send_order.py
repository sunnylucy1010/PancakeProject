import requests
import json

def send_order(order_id, access_token, image_path):

    print("Order ID: ", order_id)

    # Get the conversation ID
    get_conversation_url = "https://pos.pages.fm/api/v1/shops/30224071/orders/get_orders?access_token={access_token}".format(access_token=access_token)
    get_conversation_headers = {
        "Host": "pos.pages.fm",
        "Content-Length": "26",
        "Sec-Ch-Ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i",
        "Connection": "close"
    }

    get_conversation_data = {"search": order_id}
    get_conversation_response = requests.post(get_conversation_url, headers=get_conversation_headers, data=json.dumps(get_conversation_data))
    conversation_id = get_conversation_response.json()["data"][0]["conversation_id"]
    page_id = conversation_id.split("_")[0]

    # Upload Image to Pancake
    upload_image_url = "https://pancake.vn/api/v1/pages/{page_id}/contents?access_token={access_token}".format(page_id=page_id, access_token=access_token)
    upload_image_headers = {
        "Host": "pancake.vn",
        "Sec-Ch-Ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
        "Accept": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Origin": "https://pancake.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i",
        "Connection": "close"
    }
    upload_image_files = {
        "file": ("image.png", open(image_path, "rb"), "image/png")
    }
    upload_image_response = requests.post(upload_image_url, headers=upload_image_headers, files=upload_image_files)
    print(upload_image_response.json())
    content_url = upload_image_response.json()["content_url"]
    content_upload_status = upload_image_response.json()["success"]

    print("Content Upload Status: ", content_upload_status)
    print("Content URL: ", content_url)

    # Send Order Message
    send_message_url = "https://pages.fm/api/v1/pages/{page_id}/conversations/{conversation_id}/messages?access_token={access_token}".format(page_id=page_id, conversation_id=conversation_id, access_token=access_token)
    send_message_data = {
        "name": "sample.png",
        "mime_type": "image/png",
        "content_url": content_url,
        "attachmentType": "PHOTO",
        "action": "reply_inbox",
        "message": "",
        "thread_key": "",
    }

    send_message_response = requests.post(send_message_url, json=send_message_data)

    # https://pancake.vn/300148319853636?c_id=300148319853636_8167074529992530

    send_image_response = send_message_response.json()["success"]
    print("Send Message Status: ", send_image_response)
    send_image_response_error = None
    if send_image_response == False:
        send_image_response_error = send_message_response.json()["message"]
        print("Error: ", send_image_response_error)
    
    print("See output at: https://pancake.vn/{page_id}?c_id={conversation_id}\n".format(page_id=page_id, conversation_id=conversation_id))
    output_link = "https://pancake.vn/{page_id}?c_id={conversation_id}".format(page_id=page_id, conversation_id=conversation_id)
    return content_upload_status,send_message_response,output_link,send_image_response_error
