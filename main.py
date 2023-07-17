from flight_data import get_api_key, flight_data
from route import route
from new_flight import new_flight
import json
from times import get_etd
from passengers import pax_C208


with open('saved_routes.json') as f:
    saved = json.load(f)

saved_routes = saved['routes']

api_key = get_api_key()
payload = flight_data()
males = [4,5]
females = [3,4]
children=[1,0]
aircraft = "5YSLI"
stops = "HKNW HKMJ HKNW"
legs = route(stops)
time = "2023-07-20T16:00Z"
altitudes = [100, 110]
TOF = 1200

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
    total_pax = m + f + c
    payload['flight']['load']['passengers'] = pax_C208(m,f,c)
    payload['flight']['load']['people']= total_pax + 2
    payload['flight']['load']['cargo'] = total_pax * 33
    i+=1
    payload['flight']['alternate'] = 'HKJK'
    payload['flight']['fuel']['fuelPolicyValue'] = TOF

    flight = new_flight(api_key, payload)

    TOF = flight['flight']['performance']['fuel']['landingFuel']
    ETA = flight['flight']['performance']['times']['estimatedArrivalTime']

    ETD = get_etd(ETA)

    payload['flight']['scheduledTimeOfDeparture'] = ETD


    print(f'flight {leg} created')



