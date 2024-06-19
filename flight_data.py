import json

def flight_data():
    with open('create_flight.json') as f:
        payload = json.load(f)
    return payload

##
##def update_data():
##    with open('update_flight.json') as f:
##        updated_payload = json.load(f)
##    return updated_payload


def get_api_key():
    with open('api_key.txt') as f:
        api_key = f.read()
    return api_key

