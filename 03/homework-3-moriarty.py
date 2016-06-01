# Sean Moriarty
# 2016-05-31
# Homework 3

countries = ('Micronesia', 'Bahrain', 'Chad', 'Comorosa', 'Tonga', 'England', 'Japan')
print(countries)
for country in countries:
    print(country)
countries = sorted(countries)
print(countries)
print('The first element of this list is', countries[0])
numberocountries = len(countries)
print('The second to last element of the list is', countries[numberocountries - 2])
countries.remove('Comorosa')
print("The new list minus that one country we don't like is this")
for country in countries:
    print(country)
print("We didn't need them anyway")

tree = {'name': 'Hundred Horse Chestnut', 'species': 'Sweet Chestnut', 'age': '3000', 'location_name': 'Mount Etna, Italy', 'latitude': '37.750342', 'longitude': '15.130423'}
print(tree['name'], 'is a', tree['age'], 'year old tree that lives in', tree['location_name'])
if float(tree['latitude']) < 40.7128:
    print('The tree', tree['name'], 'in', tree['location_name'], 'is south of NYC')
else:
    print('The tree', tree['name'], 'in', tree['location_name'], 'is north of NYC')
age = input('Just how old are you, anyway? ')
if (int(age) > int(tree['age'])):
    print('You are', (int(age) - int(tree['age'])), 'years older than that tree')
else:
    print('That there tree was ', (int(tree['age']) - int(age)), 'years old when you were born')

cities = [
            {'name': 'Moscow', 'latitude': '55.7558', 'longitude': '37.6173'},
            {'name': 'Tehran', 'latitude': '35.6892', 'longitude': '51.3890'},
            {'name': 'Falkland Islands', 'latitude': '-51.7963', 'longitude': '-59.5236'},
            {'name': 'Seoul', 'latitude': '37.5665', 'longitude': '126.9780'},
            {'name': 'Santiago', 'latitude': '-33.4489', 'longitude': '-70.6693'}
]

for city in cities:
    if city['name'] == 'Falkland Islands':
        print('The Falkland Islands are a biogeographical part of the mild Antarctic zone')
    elif float(city['latitude']) > 0:
        print(city['name'], 'is above the equator')
    else:
        print(city['name'], 'is below the equator')
