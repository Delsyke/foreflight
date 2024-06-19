import requests
import json

create_link = 'https://public-api.foreflight.com/public/api/flights'


def new_flight(api_key, flight_data):
	data1 = json.dumps(flight_data)
	flight = requests.post(create_link,
		data = data1,
		headers = {
		'x-api-key':api_key,
		'Content-Type':'Application/Json'
		}
		).json()

	return flight


def update_flight(api_key, updated_data, flight_id):
    data2 = json.dumps(updated_data)
    update_link = create_link + '/' + flight_id + '?forceUpdate=True'
    updated_flight = requests.post(update_link,
        data = data2,
        headers = {
        'x-api-key':api_key,
        'Content-Type':'Application/Json'
        }
        ).json()

    return updated_flight



def refuel(stop):
    fuel_qty = int(input(f'Fuel Quantity at {stop}: '))
    print(f'Refuelled to {fuel_qty}lbs at {stop}')
    return fuel_qty


def change_alternate():
    new_alternate = input('Select Alternate: ').upper()
    print(f'Alternate changed to {new_alternate}')
    return new_alternate
