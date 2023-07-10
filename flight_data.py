import json

def flight_data():
    with open('create_flight.json') as f:
        payload = json.load(f)
    return payload


def get_api_key():
    with open('api_key.txt') as f:
        api_key = f.read()
    return api_key

