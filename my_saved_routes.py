import json
import requests
from flight_data import get_api_key

link = 'https://public-api.foreflight.com/public/api/savedroutes'
api_key = get_api_key()

def get_saved_routes():
	r = requests.get(link,
		headers = {
		'x-api-key':api_key,
		'Content-Type':'Application/Json'
		}
		).json()

	routes = json.dumps(r, indent=2)

	with open('saved_routes.json', 'w') as f:
		f.write(routes)


# get_saved_routes()