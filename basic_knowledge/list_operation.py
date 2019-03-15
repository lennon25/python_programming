#!/usr/bin/env python3

magicians = ['alice', 'david', 'carolina']
for mgn in magicians:
    print(mgn)


for mgn in magicians:
    print(mgn.title()+ ", that was a great trick!")
    print("I cam't wait to see your next trick, " + mgn.title() + '.\n')

print("Thank you, everyone, That was a great magic show!")


# 创建数值列表
# 使用函数range()
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)


# 对数字执行简单的统计运算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)


# Python切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

for player in players[0:3]:
    print(player)

my_foods = ['pizza', 'falafel', 'carrot_cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\n My friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)


# 元组（为不可变的列表）
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 不支持
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)




















