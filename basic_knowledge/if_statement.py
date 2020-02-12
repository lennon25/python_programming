#!/usr/bin/env python3
# -* coding:utf-8 -*-


# if 语句

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies')


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ', you can post a response if you wish')

age = 19
if age >= 18:
    print("You age old enough to vote!")


# if-else 语句
age = 17
if age >= 18:
    print("You age old enough to vote!")
else:
    print("Sorry, you are too yong to vote.")
    print("please register to vote as soon as you turn 18!")


# if-elif-else

age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("You admission cost is $" + str(price) + ".")


if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

alien_color = 'blue'

if alien_color == 'red':
    print("Your score is 5")
elif alien_color == 'yellow':
    print("Your score is 10")
else:
    print("Your score is 15")

age = 65

if age < 2:
    print("you is a baby")
elif age < 4:
    print("you is a one's second childhood")
elif age < 13:
    print("you is a child")
elif age < 20:
    print("you is a teenager")
elif age < 65:
    print("you is a adult")
else:
    print("you is a old man")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in requested_toppings:
    print("Adding " + topping + ".")
print("\nFinished making your pizza")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")






