#!/usr/bin/env python3


# 输入函数input()

'''
n ame = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print("\nHello, " + name + "!")


# 使用int()获取数值输入
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older")
'''

# 取余运算符
number = input("Enter a number, and I'll tell you if it's even or add: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")


# while循环
number = 1
while number <= 5:
    print(number)
    number += 1


prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


# 使用break退出循环
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# 在循环中使用continue
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue

    print(number)


# 使用while循环来处理列表和字典
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

print("\nThe follwing users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除包含特定值得列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)


# 使用用户输入来填充字典
responses = {}

polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes/ no)")
    if repeat == 'no':
        polling_active = False

print("\n ---- Polling Results ---")
for name, responses in responses.items():
    print(name + " Would like to climb " + responses + ".")



