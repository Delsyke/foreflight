def route(stops):
    strips = stops.split()
    legs = []

    for i in range(len(strips)-1):
        leg = (strips[i], strips[i+1])
        legs.append(leg)

    return legs 





