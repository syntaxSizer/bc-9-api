import urllib3
import json


city_name = ['Nairobi', 'Lagos', 'London', 'Khartom',
             'Tel aviv', 'Kampala', 'Bagdad', 'Cairo', 'Kigali']
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
API = "2bc3e79bb974a007818864813f53fd35"


def get_details(city_name):
    '''
    program that desplay weather condition
    '''

    http = urllib3.PoolManager()
    request = http.request('GET', BASE_URL,
                           fields={
                               'q': city_name,
                               'units': 'metric',
                               'appid': API
                           })
    response = json.loads(request.data.decode('utf-8'))
    # format the output
    return '{} {}'.format(str(response['weather'][0]
                              ['description']).ljust(20), str(response['main']['temp']).ljust(20))
print 'descriptions'.ljust(20), 'temperature'.ljust(20), 'city'.ljust(20), '\n' + "=" * 50
# loop in the cites
for city in city_name:
    print get_details(city), city.ljust(20)
