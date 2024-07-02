import json


with open('create_flight.json') as f:
    flight_details = json.load(f)

##with open('update_flight.json') as f:
##    update_details = json.load(f)

with open('names.json','r') as f:
    all_crew=json.load(f)


def edit_create_flight(name1, name2, all_crew, callsign):
    for crew in all_crew:
        PIC = crew['fullname'].lower()
        if PIC.startswith(name1.lower()) or PIC.endswith(name1.lower()):
            pic_user = crew['username']
            flight_details['flight']['crew'][0]['crewId'] = pic_user
            break


    for crew in all_crew:
        SIC = crew['fullname'].lower()
        if SIC.startswith(name2.lower()) or SIC.endswith(name2.lower()):
            sic_user = crew['username']
            flight_details['flight']['crew'][1]['crewId'] = sic_user
            break

    flight_details['flight']['callsign'] = callsign

    updated_create_flight = json.dumps(flight_details, indent=2)

    with open('create_flight.json', 'w') as f:
        f.write(updated_create_flight)


##    with open('update_flight.json', 'w') as f:
##        f.write(updated_update_flight)


    return 1




##crews = edit_crew_usernames('matu', 'ian', all_crew)
##print(crews)





