import pandas as pd
import os
import datetime


def plan_info():
    df = pd.read_excel('info.xlsx', 'PLAN_INFO')
    info = dict()

    route = list(df.iloc[0][1:])
    info['route'] = ' '.join(route)
    info['males'] = list(df.iloc[1][1:].dropna())
    info['females'] = list(df.iloc[2][1:].dropna())
    info['children'] = list(df.iloc[3][1:].dropna())
    info['freights'] = list(df.iloc[4][1:].dropna())
    info['altitudes'] = list(df.iloc[5][1:].dropna())
    date = df.iloc[6][1]
##    print(date)
    time = df.iloc[7][1]
    date_str = datetime.date.strftime(date, '%Y-%m-%d')
    time_str = datetime.time.strftime(time, '%H:%M:%SZ')
    info['time'] = date_str+'T'+time_str
    info['aircraft'] = df.iloc[8][1]
    info['callsign'] = df.iloc[9][1]
    info['refuel_stops'] = df.iloc[10][1]
    info['pic'] = df.iloc[11][1]
    info['sic'] = df.iloc[11][2]
    info['tof'] = df.iloc[12][1]

##    print(info)


    return info

##plan_info()