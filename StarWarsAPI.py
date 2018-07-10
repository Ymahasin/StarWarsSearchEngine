import requests

swapi_address = 'https://swapi.co/api/'

# todo clean this up

print('\nStar Wars Search: ')

'''
    json_data = requests.get(swapi_address).json()
    wDescription = json_data['results']
    print(wDescription)
'''


level1 = input('\n(try "person,luke" or "planet,tatooine" )')

level1 = level1.lower().split(',')

if level1[0] == 'person' or 'people' or 'actor' or 'character':
    level1[0] = 'people'

elif level1[0] == 'planet' or 'place' or 'location':
    level1[0] = 'planets'

elif level1[0] == 'films' or 'movie' or 'film':
    level1[0] = 'films'

elif level1[0] == 'species' or 'type' or 'creature' or 'being':
    level1[0] = 'species'

elif level1[0] == 'vehicle' or 'vehicles' or 'machine' or 'ground':
    level1[0] = 'vehicles'

elif level1[0] == 'star' or 'starship' or 'ship' or 'plane' or 'cruiser':
    level1[0] = 'starships'


print(level1[0], level1[1])

i = 0

swapi_address = 'https://swapi.co/api/' + level1[0]

json_data = requests.get(swapi_address).json()
level2start = json_data['results'][i]['name']
'''
for i in level2start:
    if json_data['results'][i]['name'] == level1[1]:
        level2start = json_data['results'][i]
    else:
        i = i + 1
'''
print(level2start)
