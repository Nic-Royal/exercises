# prog 1
'''for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end=',')'''

# prog 2
'''ask_num = int(input("Enter the number:  "))

factorial = 1
for i in range(1, ask_num + 1):
    factorial = factorial * i
print("The factorial of the %i is %i."%(ask_num, factorial))'''


# prog 3
'''dic = {}

ask_number = int(input("Type the number:  "))

for i in range(1, ask_number + 1):
    dic[i] = i * i

print(dic)'''


# prog 4
'''take_input = input('Type the nubers in list with comma:  ')
li = list(take_input.split(','))
tup = tuple(take_input.split(','))
print(li)
print(tup)'''


# prog 5
'''class two:
    ask_string = input("What is your name? ")
    capital = ask_string.upper()

string = two()
# print(string.ask_string)
print(string.capital)'''

# prog 6
'''import math
c = 50
h = 30
li = []
ask_num = input("Type the number you want to type with space: ")
new_li = list(ask_num.split())
new_li = [int(i) for i in new_li]
# print(new_li)

for d in new_li:
    value = li.append(str(round(math.sqrt((2 * c * d) / h))))
    # print(type(value))

print(','.join(li))
# print(li)'''


# prog 7
give_num = input("Type the number with comma between: ")
li = list(give_num.split(','))
li = [int(i) for i in li]
# row_num = int(give_num[0])
# col_num = int(give_num[1])
row_num = li[0]
col_num = li[1]

big_list = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        big_list[row][col] = row * col
        
print(big_list)



# prog 8
'''ask_words = input("Type the words with space in between: ")
words = list(ask_words.split())
# print(words)
words.sort()
print(','.join(words))'''



# prog 9 
'''li = []
data = True
while data:
    lines = input("What you have in your mind? ")
    li.append(lines)
    for sentence in li:
        print(sentence.upper())
        data = False
print(li)'''