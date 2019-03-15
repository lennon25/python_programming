#!/us/bin/env python3
# -*- coding:utf-8 -*-

print("Hello, World!")
print("Hello Python world!")

message = "Hello Python world!"
print(message)

message = "Hello Python crash course world!"
print(message)


# 字符串
"This is a string."
'this is a string'
message = "this is a 'Python' string."
print(message)

# 使用方法修改字符串
name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name)
print('Hello, ' + full_name.title() + '!')
message = 'Hello, ' + full_name.title() + '!'
print(message)

print('python')
print('\tpython')
print('Languages:\nPython\nC#\nJavaScript')
print('Languages:\n\tPython\n\tC\n\tJavaScript')

favorite_languages = " Python "
print(favorite_languages)
print(favorite_languages.rstrip())
print(favorite_languages.lstrip())
print(favorite_languages.strip())

message = "One of python's strengths is its diverse community."
print(message)


print(1+2)
print(0.1 + 0.1)
print(0.2 + 0.1)
print(3 * 0.1)


age = 23
print('Happy ' + str(age) + 'rd birthday!')
