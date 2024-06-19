from flight_data import get_api_key, flight_data
from route import route
from new_flight import new_flight, update_flight, refuel, change_alternate
import json
from times import get_etd
from passengers import pax_C208
from read_crew import edit_crew_usernames
from plan_info import plan_info
import datetime


api_key = get_api_key()

with open('saved_routes.json') as f:
    saved = json.load(f)
saved_routes = saved['routes']

with open('names.json') as f:
    all_crew=json.load(f)

info = plan_info()
pic = info['pic']
sic = info['sic']

# __________________________________________________________________________
# EDIT THIS SECTION

edit_crew_usernames(pic, sic, all_crew)
males = info['males']
females = info['females']
children = info['children']
freights = info['freights']
aircraft = info['aircraft']
stops = info['route']
time = info['time']
altitudes = info['altitudes']
TOF = info['tof']
refuel_stops = info['refuel_stops']
# _____________________________________________

legs = route(stops)
payload = flight_data()
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
    fr = freights[i]
    total_pax = m + f + c
    payload['flight']['load']['passengers'] = pax_C208(m,f,c)
    payload['flight']['load']['people']= total_pax + 2
    payload['flight']['load']['cargo'] = fr + total_pax*33

    i+=1

    payload['flight']['alternate'] = 'HKJK'
    payload['flight']['fuel']['fuelPolicyValue'] = TOF

    flight = new_flight(api_key, payload)
    flight_id = flight['flight']['flightId']
    minFuel = flight['flight']['performance']['fuel']['totalFuel']
    trip_fuel = flight['flight']['performance']['fuel']['fuelToDestination']
    landing_fuel = flight['flight']['performance']['fuel']['landingFuel']


    if TOF >= minFuel and TOF > 600:
        print(f'flight {leg} created')
        print(TOF, trip_fuel, landing_fuel)
        TOF = landing_fuel
        ETA = flight['flight']['performance']['times']['estimatedArrivalTime']
        ETD = get_etd(ETA)

    else:
        if leg[0] in refuel_stops and TOF < 600:
            fuel_qty = refuel(leg[0])

            payload['flight']['fuel']['fuelPolicyValue'] = fuel_qty
            updated_flight = update_flight(api_key, payload, flight_id)
            trip_fuel = updated_flight['flight']['performance']['fuel']['fuelToDestination']
            landing_fuel = updated_flight['flight']['performance']['fuel']['landingFuel']

            print(f'flight {leg} created after refuel')
            print(fuel_qty, trip_fuel, landing_fuel)

        else:
            if leg[1] != "HKNW":
                new_alternate = change_alternate()
                payload['flight']['alternate'] = new_alternate
                updated_flight = update_flight(api_key, payload, flight_id)

                trip_fuel = updated_flight['flight']['performance']['fuel']['fuelToDestination']
                landing_fuel = updated_flight['flight']['performance']['fuel']['landingFuel']

                print(f'flight {leg} created after change of alternate')
                print(TOF, trip_fuel, landing_fuel)


        TOF = landing_fuel
        ETA = updated_flight['flight']['performance']['times']['estimatedArrivalTime']
        ETD = get_etd(ETA)


    payload['flight']['scheduledTimeOfDeparture'] = ETD







