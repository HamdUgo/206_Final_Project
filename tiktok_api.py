import json

    
#saves data from API to a JSON file
def save_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

#updates JSON file with new data
def update_json(new_data, file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except:
        data = []
    
    data.extend(new_data)

    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
