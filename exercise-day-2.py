# prog 1
'''for i in range(0, 10):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1'''


# prog 2
'''for i in range(10, -4, -1):
    print(i)
    

i = 10
while i >= 0:
    print(i)
    i -= 1
'''

# prog 3
'''for i in range(0, 7):
    for j in range(0, i+1):
        print('#',end=" ")
    print()'''

# prog 4
'''for i in range(0, 7+1):
    for j in range(0, 7+1):
        if i > 1:
            print('#', end=" ")
        else:
            print('#', end=" ")
    print()'''


# prog 5
'''li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in li:
    j = i * i
    print(f'{i} x {i} = {j}')'''


# prog 6
'''li = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in li:
    print(item)'''


# prog 7
'''for i in range(0, 100, 2):
    print(i)'''


# prog 8 
'''for i in range(1, 100, 2):
    print(i)'''


# prog 9
'''total = 0
for i in range(0, 101):
    total = i + total
    # total += i
print('The sum of all numbers is %i.'%(total))'''


# prog 10
'''list_1 = [1, 2, 3, 4, 5]
list_2 = ['A', 'B', 'C', 'D']

list_1.reverse()
print(list_1)
list_2.reverse()
print(list_2)'''


# prog 10
'''list_1 = ['a', 'b', 'c', 'd', 'e']
list_2 = []
def capitalize_list_items(list_1):
    for i in list_1:
        j = i.capitalize()
        list_2.append(j)
    print(list_2)

capitalize_list_items(list_1)'''



# prog 11
'''food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(food_staff)
item = input("Type the word you want to add:  ").capitalize()
def add_item(food_staff, item):
    # for item in food_staff:
    food_staff.append(item)
    print(food_staff)
add_item(food_staff, item)
'''

# prog 12
'''food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(food_staff)
item = input("Type the word you want to remove from printed list:  ").capitalize()
def remove_item(food_staff, item):
    food_staff.remove(item)
    print(food_staff)
remove_item(food_staff, item)'''



# prog 13
'''number = int(input('Type the number:   '))
def sum_of_numbers(number):
    total = 0
    for i in range(0, number + 1):
        total += i
    print(total)
sum_of_numbers(number)'''


# prog 14
'''number = int(input("Type the number:  "))
def sum_of_odds(number):
    total = 0
    for i in range(1, number, 2):
        total += i
    print(total)
sum_of_odds(number)'''


# prog 15
'''even = 0
for num in range(0, 101, 2):
    even += num
print("The sum of all evens is %i."%(even))

odd = 0
for num in range(1, 101, 2):
    odd += num
print("The sum of all odds is %i."%(odd))'''


# prog 17
'''fruit_list = ['banana', 'orange', 'mango', 'lemon']
i = len(fruit_list) - 1
while i >= 0:
    print(fruit_list[i])
    i -= 1'''
# without loop we can do this by below code
# print(fruit_list[::-1])