#!/usr/bin/env python3

# 定义函数


def greet_user():
    print("Hello!")


greet_user()


# 向函数传递信息
def greet_user(username):
    print("Hello, " + username.title() + "!")


greet_user("Lennon")


# 实参和形参
# 位置实参
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet("dog", "willie")


# 关键字实参
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# 默认值参数
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')
describe_pet('willie')


# 返回值
def get_formatted_name(first_name, last_name):
    full_name = first_name + '.' + last_name
    return full_name.title()


musician = get_formatted_name('Lennon', 'Wang')
print(musician)


# 让实参编程可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + '.' + middle_name + '.' + last_name
    else:
        full_name = first_name + '.' + last_name
    return full_name.title()


musician = get_formatted_name('Lennon', 'Wang', 'Lin')
print(musician)
musician = get_formatted_name('Lennon', 'Wang')
print(musician)


# 返回字典
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('Lennon', 'Wang', age='27')
print(musician)


# 使用函数和while循环
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


# 传递列表
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['lennon', 'ty', 'margot']
greet_users(usernames)


# 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


# 禁止函数修改列表
print_models(unprinted_designs[:], completed_models)


# 传递任意数量的实参
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Lennon', 'wang',
                             location='princeton',
                             field='physics')
print(user_profile)


# 函数编写指南
# 1.使用小写字母和下划线命名函数名
# 2.在函数定义后一行使用文档字符串注释
# def function_name(parameter_0, parameter_1='default value')
# function_name(value_0, parameter_1='value')
# def function_name(
#        parameter_0, parameter_1, parameter_2,
#        parameter_3, parameter_4, parameter_5):
#    function body
