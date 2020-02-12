#!/usr/bin/env python3

""" 文件和异常 """

import json


# 10.1 从文件中读取文件
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)


# 10.1.2 文件路径
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())


# 10.1.3 逐行读取
filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


# 10.1.4 创建一个包含文件各行内容的列表
filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)
for line in lines:
    print(line.rstrip())


# 10.1.5 使用文件的内容
filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


# 写入文件
filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming.')

# 写入多行
filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love program.\n')
    file_object.write('I love creating new games.\n')


# 附加到文件
with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love crating apps that can run in a browser.\n')


# 异常
# 处理ZeroDivisionError异常
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")


# 使用异常避免崩溃
print("Give me two numbers, and I'll divide them")
print("Enter 'q' to quit")

while True:
    first_number = input('\nFirst number:')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if first_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


# 处理FileNotFoundError异常
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)


# 分析文本
filename = 'text_files/devb_ota_debug.log'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + "has about " + str(num_words) + " words.")


# 使用多个文件
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents =f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + "has about " + str(num_words) + " words")


filename = 'text_files/devb_ota_debug.log'
count_words(filename)
filenames = ['text_files/devb_ota_debug.log', 'text_files/pi_digits.txt', 'text_files/programming.txt']
for filename in filenames:
    count_words(filename)


# 10.4 存储数据
# 10.4.1 使用json.dump()和json.load()
numbers = [2, 3, 5, 7, 11, 13]
filename = 'text_files/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)


with open(filename, 'r') as f_obj:
    numbers1 = json.load(f_obj)

print(numbers1)


# 保存和读取用户生成的数据
username = input("What is your name? ")
filename = 'text_files/username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")


filename = 'text_files/username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")


# 10.4.3 重构
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = "text_files/username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name ?")
    filename = "text_files/username.json"
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户， 并指出名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
