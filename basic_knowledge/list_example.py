#!/usr/bin/env python3

# 列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[3])
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[2].title() + '.'
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)


# 从列表中插入元素
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

motorcycles.insert(0, 'toyota')
print(motorcycles)


# 从列表中删除元素
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# 使用pop删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

first_owned = motorcycles.pop(0)
print('The first motorcycles I owned was a ' + first_owned.title() + '.')

# 使用值 remove()删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


# 列表排序
cars = ['bmw', 'audi', 'toyota', 'tesla']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# 使用sorted()对列表临时排序
cars = ['bmw', 'audi', 'toyota', 'tesla']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list:")
print(cars)

cars.reverse()
print(cars)

# 确定列表的长度
print(len(cars))

# 尽量避免索引错误
motorcycles1 = ['honda', 'yamaha', 'suzuki']
print(motorcycles1[2])
print(motorcycles[-1])


















