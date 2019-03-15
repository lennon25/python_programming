#!/usr/bin/env python3

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


new_points = alien_0['points']
print("You just earned " + str(new_points) + "points!")

alien_0 = {'cocor': 'green', 'position': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = "yellow"
print("The alien is now " + alien_0['color'] + ".")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))


if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))


# 删除键-值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      '.')


# 遍历字典
user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user.items():
    print("\nkey: " + key)
    print("Value: " + value)

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite languages is " + language.title() + ".")


# 遍历字典中的所有键

for name in favorite_languages.keys():
    print(name.title())


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")


# 按顺序遍历字典的所有键
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll")

# 遍历字典的的所有值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 剔除遍历的重复项
for language in set(favorite_languages.values()):
    print(language.title())


# 嵌套
# 列表存储字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:5]:
    print(alien)
print("...")


# 字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print("You ordered a " + pizza['crust'] + "-crust pizza" + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print("\n" + name.title() + "'s favorite languages is:")
    else:
        print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
            print("\t" + language.title())


# 字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'enistein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tlocation: " + location.title())


# 练习
favorite_places = {
    'lennon': ['shenzhen', 'hongkong', 'chognqing'],
    'congcong': ['shenzhen', 'xizang', 'qinghai'],
    }
for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())

cities = {
    'beijing': {
        'country': 'china',
        'population': '2171W',
        'fact': 'political center',
        },
    'shenzhen': {
        'country': 'china',
        'population': '1252.83W',
        'fact': 'technology center',
        },
    'new york': {
        'country': 'america',
        'population': '851W',
        'fact': 'port city',
        },
    }

for city, city_info in cities.items():
    print("\nCity: " + city)
    print("\t Country: " + city_info['country'].title())
    print("\t Population: " + city_info['population'].title())
    print("\t fact: " + city_info['fact'].title())

