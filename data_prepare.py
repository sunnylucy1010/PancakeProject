import requests
import json

url = 'https://pro.api.anousith.express/graphql'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://app.anousith-express.com/',
    'Content-Type': 'application/json',
    'Authorization': 'undefined',
    'Origin': 'https://app.anousith-express.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Te': 'trailers'
}

data = {
    "operationName": "CustomerLogin",
    "variables": {
        "where": {
            "username": "96460888",
            "password": "96460888"
        }
    },
    "query": "mutation CustomerLogin($where: CustomerLoginInput!) {\n  customerLogin(where: $where) {\n    accessToken\n    data {\n      id_list\n      full_name\n      profile_img\n      start_work_time\n      status\n      added_user\n      username\n      contact_info\n      address\n      village\n      district {\n        id_list\n        id_state {\n          provinceName\n          id_state\n        }\n        title\n      }\n      state {\n        provinceName\n        id_state\n      }\n      Bank_KIP\n      BANK_THB\n      BANK_USD\n      BANK_NAME\n      chargeOnShop\n      ip_address\n      appid\n      app_device\n      services\n      level\n      staff_branch_id\n      gender\n      isActive\n    }\n  }\n}"
}

response = requests.post(url, headers=headers, json=data)

atoken = response.json()['data']['customerLogin']['accessToken']

url = 'https://pro.api.anousith.express/graphql'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://app.anousith-express.com/',
    'Content-Type': 'application/json',
    'Authorization': '%s' % atoken,
    'Origin': 'https://app.anousith-express.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Te': 'trailers'
}

data = {
    "operationName": "ItemsV2",
    "variables": {
        "where": {
            "customerId": 358218,
            "isDeleted": 0,
            "originReceiveDate_gte": "2024-05-10",
            "originReceiveDate_lt": "2024-05-11",
            "multipleItemStatus": ["TRANSIT_TO_DEST_BRANCH", "TRANSIT_TO_ORIGIN_BRANCH", "DEST_BRANCH_RECEIVED_FORWARD", "ORIGIN_BRANCH_RECEIVED_BACKWARD", "DEST_BRANCH_RECEIVED_BACKWARD", "ORIGIN_BRANCH_RECEIVED_FORWARD", "COMPLETED"],
            "searchMultipleCOD": ["0", "1"]
        },
        "orderBy": "originReceiveDate_DESC",
        "skip": 0,
        "limit": 5
    },
    "query": "query ItemsV2($where: ItemV2WhereInput, $skip: Int, $noLimit: Boolean, $limit: Int, $orderBy: OrderByItem) {\n  itemsV2(\n    where: $where\n    skip: $skip\n    noLimit: $noLimit\n    limit: $limit\n    orderBy: $orderBy\n  ) {\n    total\n    data {\n      _id\n      trackingId\n      itemName\n      itemValueKIP\n      itemValueTHB\n      itemValueUSD\n      realItemValueKIP\n      realItemValueTHB\n      realItemValueUSD\n      receiverName\n      receiverPhone\n      description\n      isSummary\n      charge_on_shop\n      itemStatus\n      contactStatus\n      originSendDate\n      width\n      weight\n      isCod\n      isExtraItem\n      packagePrice\n      isDeposit\n      originReceiveDate\n      destReceiveDate\n      sendCompleteDate\n      isBackward\n      billNumber\n      originProvinceId {\n        provinceName\n      }\n      destProvinceId {\n        provinceName\n      }\n      originBranchId {\n        branch_name\n      }\n      destBranchId {\n        branch_name\n        branch_address\n        districtName\n        contactInfo\n      }\n      customerId {\n        id_list\n        full_name\n        contact_info\n      }\n      createdBy {\n        first_name\n        phone_number\n      }\n      originReceiveBy {\n        first_name\n        phone_number\n      }\n    }\n  }\n}"
}

response = requests.post(url, headers=headers, json=data)

result = response.json()

raw_data = result['data']['itemsV2']['data']

print(raw_data)
# keys_to_keep = ["trackingId", "_id"]

# filtered_data = [{key: item[key] for key in keys_to_keep} for item in raw_data]
# # Save filtered_data to a JSON file
# with open('filtered_data.json', 'w') as f:
#     json.dump(filtered_data, f)
  