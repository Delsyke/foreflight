import requests
import json

link = 'https://public-api.foreflight.com/public/api/flights'

def new_flight(api_key, flight_data):
	data = json.dumps(flight_data)
	flight = requests.post(link,
		data = data,
		headers = {
		'x-api-key':api_key,
		'Content-Type':'Application/Json'
		}
		).json()

	return flight




