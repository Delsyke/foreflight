from datetime import datetime

def get_etd(eta):
	eta_str = eta[0:19]+'Z'
	
	ETA = datetime.strptime(eta_str, '%Y-%m-%dT%H:%M:%SZ')
	ground_time = timedelta(minutes=15)
	ETD = ETA+ground_time
	ETD_str = datetime.strftime(ETD, '%Y-%m-%dT%H:%M:%SZ')
	return ETD_str


# etd = get_etd(t)
# print(etd, type(etd))