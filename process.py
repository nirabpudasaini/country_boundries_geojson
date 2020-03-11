import json
import requests

BASE_URL = 'https://github.com/simonepri/geo-maps/releases/latest/download/'
# Required countries 
# UK - GBR, Ireland - IRL, Germany - DEU, Greece - GRC, Finland - FIN, 
# Bulgaria - BGR, Hungary - HUN, Malta - MLT, Italy - ITA
COUNTRIES = [
    ['GBR', 'uk'], 
    ['IRL', 'ierland'], 
    ['DEU', 'germany'], 
    ['GRC', 'greece'], 
    ['FIN', 'finland'], 
    ['BGR', 'bulgaria'], 
    ['HUN', 'hungary'], 
    ['MLT', 'malta'], 
    ['ITA', 'italy']
]

def get_data_from_url(filename):
    print('Fetching ', filename)
    url = BASE_URL + filename
    r = requests.get(url)
    data = r.json()
    return data

def filter_required_countries(data, type_of_data):
    print('Extracting required countries')
    output = []
    features = data['features']
    required_countries = []
    for country in COUNTRIES:
        required_countries.append(country[0])
    for feature in features:
        if feature['properties']['A3'] in required_countries:
            feature['properties']['type'] = type_of_data
            output.append(feature)
    return output

def generate_country_polygons(data):
    output = {
        "type": "FeatureCollection",
        "features": []
    }
    for country in COUNTRIES:
        for items in data:
            if items['properties']['A3'] == country[0]:
                output['features'].append(items)
        print ('writing data for ', country[1])
        with open('data/' + country[1] + '.geo.json', 'w') as file:
            json.dump(output, file)
        output['features'] = []    
                    
def process_data(resolution):
    coastline = 'countries-coastline-' + resolution + '.geo.json'
    coastline_data = get_data_from_url(coastline)
    land = 'countries-land-' + resolution + '.geo.json'
    land_data = get_data_from_url(land)    
    
    filtered_coastline_data = filter_required_countries(coastline_data, 'coastline')
    filtered_land_data = filter_required_countries(land_data, 'land')
    filtered_data = filtered_coastline_data + filtered_land_data

    generate_country_polygons(filtered_data)

    # with open(outputpath, 'w') as file:
    #     json.dump(output, file)
    # print('Got data for ',len(output['features']), ' countries')

process_data('1m')
