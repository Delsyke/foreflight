import json
import requests
from flight_data import get_api_key, flight_data
from route import route
from new_flight import new_flight


api_key = get_api_key()
payload = flight_data()
males = [4,5,0]
females = [3,4,3]
children=[0,0,3]
aircraft = "5YSLL"
stops = "HKNW HKFH HKAM HKNW"
legs = route(stops)
time = "2023-07-10T15:00:00Z"
altitudes = [110, 100, 100]
TOF = 1300

payload['flight']['scheduledTimeOfDeparture'] = time
payload['flight']['aircraftRegistration'] = aircraft
i=0

for leg in legs:
    payload['flight']['departure'] = leg[0]
    payload['flight']['destination'] = leg[1]
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



