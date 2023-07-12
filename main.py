from flight_data import get_api_key, flight_data
from route import route
from new_flight import new_flight
import json


with open('saved_routes.json') as f:
    saved = json.load(f)

saved_routes = saved['routes']

api_key = get_api_key()
payload = flight_data()
males = [4,5,0]
females = [3,4,3]
children=[0,0,3]
aircraft = "5YSLN"
stops = "HKNW HKAK HKMF HKNW"
legs = route(stops)
time = "2023-07-13T16:00:00Z"
altitudes = [110, 100, 100]
TOF = 1300

payload['flight']['scheduledTimeOfDeparture'] = time
payload['flight']['aircraftRegistration'] = aircraft
i=0

for leg in legs:
    payload['flight']['departure'] = leg[0]
    payload['flight']['destination'] = leg[1]

    for r in range(len(saved_routes)):
        if saved_routes[r]['departure'] == leg[0]:
            if saved_routes[r]['destination'] == leg[1]:
                saved_route = saved_routes[r]['route']
                payload['flight']['routeToDestination']['route']=saved_route
                break
    else:
        payload['flight']['routeToDestination']['route']="DCT"
    
    
    payload['flight']['routeToDestination']['altitude']['altitude'] = altitudes[i]
    m = males[i]
    f = females[i]
    c = children[i]
    pax = m + f + c
    payload['flight']['load']['people']= pax + 2
    payload['flight']['load']['cargo'] = pax * 33
    i+=1
    payload['flight']['alternate'] = 'HKJK'
    payload['flight']['fuel']['fuelPolicyValue'] = TOF

    flight = new_flight(api_key, payload)

    TOF = flight['flight']['performance']['fuel']['landingFuel']
    ETA = flight['flight']['performance']['times']['estimatedArrivalTime']
    payload['flight']['scheduledTimeOfDeparture'] = ETA


    print(f'flight {leg} created')



