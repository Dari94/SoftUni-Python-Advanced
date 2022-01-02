countries = input().split(', ')
cities = input().split(', ')

countries_cities = dict(zip(countries, cities))

for key,value in countries_cities.items():
    print(f'{key} -> {value}')