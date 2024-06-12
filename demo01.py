# coding:utf-8

# print ("hello world")
# name = "Ada Lovelace"
# print(name.upper())
# print(name.lower())

# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"

# print(full_name)
#.title()  将第一个字母大写
# print(f"hello,{full_name.title()}")

#列表
motorcycles = ['honda','yamaha','suzuki']
# #添加元素至末尾
# # motorcycles.append('ducati')
# print(motorcycles)

# #在第0位置插入元素
# motorcycles.insert(0,'ducati')
# print(motorcycles)

# #删除第0位置的元素
# del motorcycles[0]
# print(motorcycles)

#pop()删除列表末尾的元素，也叫弹出
popped_motorcycle = motorcycles.pop()
print("zzz:",motorcycles)
print("zzz:",popped_motorcycle)

# 也可以指定位置
first_owned = motorcycles.pop(0)
print(first_owned)

#直接删除指定的值
motorcycles.remove('yamaha')
print(motorcycles)

#对列表排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#按倒序排列
cars.sort(reverse=True)
print(cars)

#临时排序
print(sorted(cars))
print('原始：',cars)

#倒序
cars.reverse()
print(cars)

#range()创建数字列表
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print (squares)

#复制列表,使用[:]
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print(friend_foods)

#元组tuple，值不可变更
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# car = 'Audi'
# print(car.lower() == 'audi')
# print(car)

#字典，键值对
# alien_0 = {"color":"green","points":"5"}
# print(alien_0)
# print(alien_0['color'])

alien_0 ={}
alien_0['color'] = 'green'
alien_0['points'] = '5'
print(alien_0)

#遍历所有的键值对.items()
print(alien_0.items())
#遍历所有的键.key()
print(alien_0.keys())

#遍历所有的值.values()
print(alien_0.values())
