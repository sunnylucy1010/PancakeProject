import json

def clear_data(data_file_path):
    # Open and load the JSON file
    with open(data_file_path) as f:
        data = json.load(f)

    # Clear the 'orders' list
    data['orders'] = []

    # Write the updated data back to the JSON file
    with open(data_file_path, 'w') as f:
        json.dump(data, f, indent=4)