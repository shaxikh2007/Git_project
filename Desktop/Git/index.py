# 1 one
# print(18 ) 



# 2 one
# years = 27

# months = years * 12
# days = years * 365
# weeks = days // 7

# print("Months:", months)
# print("Days:", days)
# print("Weeks:", weeks)


# 3 one
# print(3.14*5*5)

# 4 one
# years = 18
# months = years * 12
# days = years * 365
# weeks = days // 7

# print("Months:", months)
# print("Days:", days)
# print("Weeks:", weeks)



# 5 one
# a = 12
# b = 33
# c = 42
# abc=12+33+42
# print(abc/3)

# 6 one
# a = 12
# b = 33

# sum=a+b
# diff=a-b
# prod=a*b
# quoti=a/b
# print(diff,sum,prod,quoti)



# 7 one 
# print(5**4)


# 8 one

# a = 4
# b = 56

# print(a*b)  


# Next Lesson

# name = input("Your name")
# surname = input("Your surname")
# age = input("Your age")

# print("Name:",name,"Surname:",surname,"Age:",age)



# 2 one


# name = "John"

# name = "Mike"

# print(name)



# 4 one

# date = int( input("Your birth date"))

# year = 2025

# age = year-date
 
# age = 18
# months = age * 12
# days = age * 365
# weeks = days // 7
 
# print("Months:", months)
# print("Days:", days)
# print("Weeks:", weeks)


# 5 one
# name = input("Your name")
# surname = input("Your surname")
# age = input("Your age")

# print("Name:",name,"Surname:",surname,"Age:",age)








# a = ['black','blue','grey','white']

# print(a[0],a[-1])





# a = ['black','blue','grey','white']

# a.insert(1, 'purple')
# print(a)






# grocery = ['pepsi','bread','butter','yogurt']

# print(len(grocery))






# grocery = ['pepsi','bread','butter','yogurt']

# grocery.append('cheese')

# print(grocery)



# grocery = ['pepsi','bread','butter','yogurt']

# grocery.insert(0, 'fruits')

# print(grocery)




# grocery = ['pepsi','bread','butter','yogurt','eggs']

# grocery.remove('eggs')

# print(grocery)


# grocery = ['pepsi','bread','butter','yogurt','eggs']

# grocery.pop()

# print(grocery)



# numbers = [1,5,3,6,7,8,3,1,2,6,0]

# numbers.sort()

# print(numbers)



# numbers = [1,5,3,6,7,8,3,1,2,6,0]

# numbers.reverse()

# print(numbers)




# numbers = [[1,2,3], [1,2,3], [1,2,3]]



# print(numbers)




# grocery = ['pepsi','bread','butter','yogurt','eggs']

# print(grocery)

# grocery = ['pepsi','bread','butter','yogurt','eggs']
# grocery.append('juice')
# print(grocery)




# movies = [
#     ('Avangers', 'James', 2015, "1200$"),
#     ('Avangers 2', 'James Bond', 2025,"5200$"),
#     ('Avangers 3', 'James Dan', 2035,"12200$"),
    
# ]

# print(movies)





# name = 'Jose'

# greeting = f'Hello, {name}'

# print(f'Hello {name}')




# x = '25'

# z = int(x) + 25

# print(z)




# x = '20'

# y = '10'

# text = 'pay:' + str(int(x)*int(y))

# print(text)

# and_operator = (1 > 2) and (6 < 8)  
# print(and_operator)
# equal_operator = (3 == 3) or (2 != 2) 
# print(and_operator)
# not_operator = not (5 > 10)  
# print(not_operator)

#<<<<<<<<<<<<<<<<<<< Nested fo loop >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..

# for i in range(7):
#     for j in range(i+1,7):
#         print(i,j)




# rows, cols =3,5
# for r in range(rows):
#     line=""
#     for c in range(cols):
#         line+="*"
#         print(line)
    

# n = 5
# for i in range(1, n+1):
#     print(" "*(n-i-1)+"*"*i)



# grid = [
#     [3,1,4,5,6,8],
#     [1,5,9,6,3,8]
# ]
# total = 0
# for r in range(len(grid)):
#     for c in range(len(grid[0])):
#         total += grid[r][c]
#         print(total)

# grid = [
#     [3,1,4,],
#     [1,5,9,]
# ]
# dirs = [(1,0),(-1,0),(0,1),(0,1),(0,-1)]
# R, C = len(grid), len(grid[0])
# for r in range(R):
#     for c in range(C):
#         for dr,dc in dirs:
#             nr,nc=r+dr,c+dc
#             if 0<=nr<R and 0<=nc<C:
#                 print(nr,nc)




# for i in range(3):
#     for j in range(5):
#         if j==2:
#             print(j)
#             break
            

# my_list = [1, 2, 3, 1, 4, 5, 3]

# unique_list = []

# for number in my_list:
  
#   if number not in unique_list:
#     unique_list.append(number)
    
# print(unique_list)



# print(9 / 4)
# print(9 // 4)
# print(9 % 4)
# print(3 + 5 * 2 - 3**2)




# number = "+998939379277"
# password = "secret"
# attempts = 3
# while True:
#     user_input = input("Enter password: ")
#     if user_input == password:
#         print("Login successful!")
#         break
#     else:
#         attempts -= 1
#         print(f"Incorrect password. {attempts} attempts remaining.")
#         if attempts == 0:
#             print("Account locked. Contact support. Do u want to reset it ? Yes/No")
#             reset = input()
#             if reset == "Yes":
#                 print("Enter ur number with which u have registered include +998")
#                 number_check = input()
#                 if number == number_check:
#                     print("This is correct u can reset the password")
#                     password = input("Write new password")

#                 else:
#                     print("Ur wrong")
#             else:
#                 break


# sentence = "Hello, how are you?"
# words = sentence.split(' ')
# print(words)  

            

# string = "apple,banana,orange"
# fruits = string.split(",")
# print(fruits) 


# string = "one,two,three,four,five"
# parts = string.split(",",1 )
# print(parts)  



# multiline_string = "Line 1\nLine 2\nLine 3"
# lines = multiline_string.split("\n")
# print(lines)  


            

# string = "Hello"
# characters = list(string)
# print(characters)  


# sentence = "   Hello, how are you?   "
# words = sentence.strip().split("o", 2)
# print(words) 



# sentence = "Hello, How Are You?"
# words = sentence.lower().split()
# print(words)

# string = "This is a string."
# list_of_strings = string.split("i", maxsplit=1)

# print(list_of_strings)




# words = ["Hello", "world"]
# sentence = " ".join(words)
# print(sentence) 



# numbers = [1, 2, 3]
# string = " ".join(str(number) for number in numbers)
# print(string) 


# words = ["apple", "banana", "orange"]
# string = " ".join(words)
# print(string)  


# words = ["apple", "banana", "orange"]
# string = "-".join(words)
# print(string)  


# words = ["Hello", "world"]
# string = "\n".join(words)
# print(string) 


# numbers = [1, 2, 3, 4, 5]
# sublist = numbers[1:3]
# print(sublist)



# count = 0
# while True:
#     print("Count:", count)
#     count += 1



# while True:
#  user_input = input("Enter a value (type 'exit' to stop): ")
#  if user_input.lower() == 'exit':
#     break
# print("You entered:", user_input)



# numbers = [1, 2, 3, 4, 5]
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1






# count = 0
# while count < 5:
#     count += 1
#     if count == 3:
#         continue
#     print("Count:", count)




# count = 0
# while count < 6:
#     print("Inside while loop")
#     count += 1
# else:
#     print("Inside else block")



# count = 0
# while count < 5:
#     print("Count:", count)
#     count += 1
#     if count == 3:
#         break



# n = 5
# factorial = 1
# i = 1
# while i <= n:
#     factorial *= i
#     i += 1
# print(f"Factorial of {n} is: {factorial}")
# text = ""
# while len(text) < 10:
#     text += "a"
#     print(text)



# start = 1
# end = 10
# while start <= end:
#     print(start)
#     start += 1


# outer_count = 1
# while outer_count <= 3:
#     inner_count = 1
#     while inner_count <= 3:
#         print(f"Outer: {outer_count}, Inner: {inner_count}")
#         inner_count += 1
#     outer_count += 1



# numbers = [1, 2, 3, 4, 5]
# while numbers:
#     print(numbers.pop())


# n = 5
# sum_of_numbers = 0
# while n > 0:
#     sum_of_numbers += n
#     n -= 1
# print("Sum of numbers:", sum_of_numbers)


# is_running = True
# while is_running:
#     user_input = input("Continue? (yes/no): ")
#     if user_input.lower() == 'no':
#         is_running = False
#     else:
#         print("Continuing...")





# colors = ['red', 'green', 'blue']
# index = 0
# while index < len(colors):
#     print(f"Color at index {index}: {colors[index]}")
#     index += 1


# n = 10
# a, b = 0, 1
# while n > 0:
#     print(a, end=" ")
#     a, b = b, a + b
#     n -= 1




# numbers = [x for x in range(1, 6)]
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1



# count = 1
# while count <= 5:
#     print(count,"Even" if count % 2 == 0 else "Odd")
#     count += 1



# count = -3
# while count <= 0:
#     print(count)
#     count += 1


# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 22]
# i = 0
# while i < len(names) and i < len(ages):
#     print(f"{names[i]} is {ages[i]} years old.")
#     i += 1


# string_data = "abcd"
# char1, char2, char3 = string_data
# print(char2)


# data = [7, 8, 9]
# _, _, last_element = data
# print(_)


# tuple_data = (1, 2, 3, 4, 5)
# _, _, a, _, b = tuple_data
# print(a)


# nested_tuple = ((1, 2), (3, 4))
# (a, b), (c, d) = nested_tuple
# print(a,c)




# nested_list = [[1, 2], [3, 4]]
# [a, b], [c, d] = nested_list
# print(a,c)


# list_of_tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
# for number, word in list_of_tuples:
#     print(f"{number}: {word}")

# data = [1, 2, 3, 4, 5]
# first, *rest, last = data
# print(*rest)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
#     a, b, c = row
#     print(a, b, c)



# fruits = ['apple', 'orange', 'banana']
# for index, fruit in enumerate(fruits, start=10):
#     print(index, fruit)



# word = "Python"
# for index, char in enumerate(word):
#     print(index, char)



# coordinates = [(1, 2), (3, 4), (5, 6)]
# for index, (x, y) in enumerate(coordinates):
#     print(index, x, y)


# fruits = ['apple', 'ornge', 'banana']

# for index, fruit in enumerate(fruits):
#   if 'a' in fruit:
#       print(index, fruit)


# fruits = ['apple', 'orange', 'banana']

# index = 0
# while index < len(fruits):
#     print(index, fruits[index])
#     index += 1



# fruits = ['apple', 'ornge', 'banana']
# for index, fruit in enumerate(reversed(fruits)):
#   print(index, fruit)


# fruits = ['apple', 'orange', 'banana']

# for index, fruit in enumerate(fruits):
#   print(index, fruit)
#   if fruit == 'orange':
#       break



# list1 = [1, 2, 3,]
# list2 = ['a', 'b', 'c','w']
# zipped = zip(list1, list2)
# print(list(zipped))


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# for item1, item2 in zip(list1, list2):
#   print(item1, item2)



# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# zipped = zip(list1, list2)
# unzipped1, unzipped2 = zip(*zipped)

# print(list(unzipped2))


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# zipped_range = zip(range(1, 6), list2)

# print(list(zipped_range))



# iter1 = [1, 2, 3]
# iter2 = ['a', 'b', 'c']
# iter3 = ['x', 'y', 'z']
# combined_iterables = zip(iter1, iter2, iter3)

# print(list(combined_iterables))



# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# tuple_list = list(zip(range(len(list1)), list1))

# print(list(tuple_list))



# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# for index, (item1, item2) in enumerate(zip(list1, list2)):
#     print(index, item1, item2)


# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# list3 = ['x', 'y', 'z']
# for index, (item1, item2, item3) in enumerate(zip(list1, list2, list3), 9):
#     print(index, item1, item2, item3)




# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# list3 = ['x', 'y', 'z']
# start_index = 10
# for index, (item1, item2) in enumerate(zip(list1, list2), start=start_index):
#     print(index, item1, item2)



# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# list3 = ['x', 'y', 'z']
# list4 = ['p', 'q','p']
# for index, (item1, item2, item3, item4) in enumerate(zip(list1, list2, list3, list4), start=5):
#     print(index, item1, item2, item3, item4)



# grades = {"Ali": 90, "Sara": 85, "John": 78}
# print("Ali" in grades)
# print(85 in grades)
# print(85 in grades.values())


# D = {"a": 1, "b": 2, "c": 3}
# removed = D.pop("x", "No such key")
# print(removed)
# print(D)

# numbers = [1, 2, 3, 4]
# squares = {n: n**2 for n in numbers}
# print(squares)
# print(squares[3])


# student = {
#     "name": "Anna",
#     "marks": {"math": 95, "english": 88}
# }
# print(student["marks"]["english"])
# student["marks"]["english"] = 90
# print(student)


# my_string = "Hello, world!"

# for character in my_string:
#   print("Me")

# my_list = [1, 2, 3, 4, 5]

# max_value = my_list[0]
# for number in my_list:
#   if number > max_value:
#     max_value = number

#     print(max_value)

# my_list = [5, 3, 2, 1, 4]

# sorted_list = []

# for number in sorted(my_list):
#   sorted_list.append(number)
#   print(sorted_list)


# my_list = [1, 2, 3, 1, 4, 5, 3]

# unique_list = []

# for number in my_list:
#   if number not in unique_list:
#     unique_list.append(number)

# print(unique_list)


# my_list = [1, 2, 3, 4, 5]

# filtered_list = []

# for number in my_list:
#   if number > 3:
#     filtered_list.append(number)

# print(filtered_list)


# students = [("John", 90), ("Mike", 80), ("Sarah", 95)]
# for name, grade in students:
#   print(name, grade)
# for num in range(0, 10, 2):
#   print(num)

# fruits = ['apple', 'banana', 'cherry']
# for i in range(len(fruits)):
#   print(i, fruits[i])



# matrix = [[1, 2], [3, 4]]
# for row in matrix:
#   for num in row:
#     print(num)


# numbers = [1, 2, 3]
# squares = []
# for num in numbers:
#   square = num ** 2
#   squares.append(square)
# print(squares)


# my_list = [1, 2, 3, 4, 5]

# total = 0
# for number in my_list:
#   total += number

# print(total)


# average = 0
# for number in range(1, 101):
#   average += number

# average /= 100

# print(average)


# my_list = [1, 2, 3, 4, 5]

# max_value = my_list[0]
# for index in range(1, len(my_list)):
#   if my_list[index] > max_value:
#     max_value = my_list[index]

#     print(max_value)


# my_list = [1, 2, 3, 1, 4, 5, 3]

# unique_list = []
# for index in range(len(my_list)):
#   if my_list[index] not in unique_list:
#     unique_list.append(my_list[index])

# print(unique_list)


# my_list = [1, 2, 3, 4, 5]
# for i in range(len(my_list)-1, -1, 1):
#     print(my_list[i])



# nested_list = [[1, 2], [3, 4], [5, 6]]
# for i in range(len(nested_list)):
#     for j in range(len(nested_list[i])):
#         print(nested_list[i][j])


# my_list = [i**2 for i in range(5)]
# print(my_list)

# my_list = [1, 2, 3, 4, 5]

# for number in my_list:
#   if number > 3:
#     break

# print(number)


# nested_list = [[1, 2], [3, 4], [5, 6]]
# for i in range(len(nested_list)):
#     for j in range(len(nested_list[i])):
#         print(nested_list[i][j])


# my_list1 = [1, 2, 3]
# my_list2 = [4, 5, 6]

# for number1 in my_list1:
#   for number2 in my_list2:
#     if number1 + number2 > 10:
#       break

#   print(number1)


# my_list = ["John", "Jane", "Peter", "Mary"]

# for name in my_list:
#   if name == "Mary":
    
#     break
# print(name)


# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for sublist in my_list:
#     for item in sublist:
#         if item == 5:
#             break
#         print(item)


# my_list = ['apple', 'banana', 'cherry']
# for item in my_list:
#     if len(item) > 7:
#         break
#     print(item)


# sentence = "Python is fun to learn"
# words = sentence.split()
# print(words)
# print(words[0])
# print(words[1:4])


# text = "apple,banana,orange"
# items = text.split(",")
# print(items)
# print(" & ".join(items))
# print("-".join(items[1:]))


# s = "Programming"
# print(s[0:6])
# print(s[3:])
# print(s[-5:])
# print(s[0:10:2])

# data = ("Alice", 25, "Engineer", "London")
# name, age, job, city = data
# print(name)
# print(age, job)
# print(city, "-", name)



# names = ("Mike", "Peter", "John")
# for index, name in enumerate(names, start=5):
#     print(index, name)


# students = ["Ali", "Sara", "John", "Bob"]
# scores = [90, 85, 78]
# for s, sc in zip(students, scores):
#     print(s, sc)


# grades = {"Ali": 90, "Sara": 85, "John": 78}
# grades["John"] = 88
# grades["Bob"] = 70
# print(grades["John"])
# print("Sara" in grades)
# print(grades.get("Mike", "Not"))


# prices = {"apple": 3, "banana": 2, "orange": 4}
# for item, price in prices.items():
#     print(item, "-", price)


# for i in range(1, 3):
#     for j in range(1, 4):
#         print(i, j)



# n = 4
# while n > 0:
#     print("n =", n)
#     if n == 2:
#         break
#     n -= 1
# print("after loop:", n)



# i = 1
# while i <= 3:
#     j = 1
#     while j <= i:
#         print(i, j)
#         j += 1
#     i += 1


# line = "Ali 90, Sara 85, John 78"
# parts = line.split(", ")

# names = []
# scores = []
# for part in parts:
#     name, score = part.split()
#     names.append(name)
#     scores.append(int(score))
# grades = dict(zip(names, scores))
# print(grades)
# for idx, (name, score) in enumerate(grades.items(), start=1):
#     print(idx, name, "->", score)


# text = "red,green,blue,yellow"
# colors = text.split(",")

# for i, color in enumerate(colors, start=1):
#     part = color[:3]
#     joined = "*".join(color[1:4])
#     print(i, part, joined)

# word = "PYTHON"
# i = 0

# while i < len(word):
#     j = 0
#     line = ""
#     while j <= i:
#         line += word[j]
#         j += 1
#     print(line.lower())
#     i += 1

# names = ["Ali", "Sara", "John"]
# scores = [90, 85, 78]

# grades = dict(zip(names, scores))
# grades["Sara"] = 95
# grades["Bob"] = 60

# for name, score in grades.items():
#     if score >= 80:
#         print(name, "OK")
#     else:
#         print(name, "LOW")



# data = ["Ali-90", "Sara-85", "John-78"]
# names = []
# scores = []

# for item in data:
#     name, score = item.split("-")
#     names.append(name)
#     scores.append(score)

# first, *middle, last = names

# print(first, last)
# print(middle)

# for i, (n, s) in enumerate(zip(names, scores), start=1):
#     print(f"{i}) {n[:2]} -> {str(s)[:2]}")


# sentence = "I love learning Python"
# words = "sentence.split()"

# for i in range(len(words)):
#     part = words[:i+1]
#     print(" ".join(part))


# sentence = "Python is fun to learn"
# words = sentence.split()
# print(words)
# print(words[0])
# print(words[1:6])



# text = "apple,banana,orange"
# items = text.split(",")
# print(items)
# print(" & ".join(items))
# print("-".join(items[1:2]))


# s = "Programming"
# print(s[0:6])
# print(s[3:])
# print(s[-5:])
# print(s[0:10:2])


# data = ("Alice", 25, "Engineer", "London")
# name, age, job, city = data
# print(name)
# print(age, job)
# print(city, "-", name)

# values = (10, 20, 30, 40)
# first, *middle, last = values
# print(first)
# print(middle)
# print(last)


# names = ("Mike", "Peter", "John")
# for index, name in enumerate(names, start=5):
#     print(index, name)


# students = ["Ali", "Sara", "John", "Bob"]
# scores = [90, 85, 78]
# for s, sc in zip(students, scores):
#     print(s, sc)


# grades = {"Ali": 90, "Sara": 85, "John": 78}
# grades["John"] = 88
# grades["Bob"] = 70
# print(grades["John"])
# print( 85 in grades.values())
# print(grades.get("Mike", "Not found"))


# prices = {"apple": 3, "banana": 2, "orange": 4}
# for item, price in prices.items():
#     print(item, "-", price)


# for i in range(1, 3):
#     for j in range(1, 4):
#         print(i, j)


# n = 4
# while n > 0:
#     print("n =", n)
#     if n == 2:
#         break
#     n -= 1
# print("after loop:", n)


# i = 1
# while i <= 3:
#     j = 1
#     while j <= i:
#         print(i, j)
#         j += 1
#     i += 1


# line = "Ali 90, Sara 85, John 78"
# parts = line.split(", ")

# names = []
# scores = []
# for part in parts:
#     name, score = part.split()
#     names.append(name)
#     scores.append(int(score))
# grades = dict(zip(names, scores))
# print(grades)
# for idx, (name, score) in enumerate(grades.items(), start=1):
#     print(idx, name, "->", score)


# text = "red,green,blue,yellow"
# colors = text.split(",")

# for i, color in enumerate(colors, start=1):
#     part = color[:3]
#     joined = "*".join(color[1:4])
#     print(i, part, joined)


# word = "PYTHON"
# i = 0

# while i < len(word):
#     j = 0
#     line = ""
#     while j <= i:
#         line += word[j]
#         j += 1
#     print(line.lower())
#     i += 1

# names = ["Ali", "Sara", "John"]
# scores = [90, 85, 78]

# grades = dict(zip(names, scores))
# grades["Sara"] = 95
# grades["Bob"] = 60

# for name, score in grades.items():
#     if score >= 80:
#         print(name, "OK")
#     else:
#         print(name, "LOW")


# data = ["Ali-90", "Sara-85", "John-78"]
# names = []
# scores = []

# for item in data:
#     name, score = item.split("-")
#     names.append(name)
#     scores.append(int(score))

# first, *middle, last = names

# print(first, last)
# print(middle)

# for i, (n, s) in enumerate(zip(names, scores), start=1):
#     print(f"{i}) {n[:2]} -> {str(s)[:2]}")


# sentence = "I love learning Python"
# words = sentence.split()

# for i in range(len(words)):
#     part = words[:i+1]
#     print(" ".join(part))


# x = int(input("Write the number"))
# def pos(x):
#     if x<0:
#         print("This number is negative!")
#     else:
#         print("This number is Positive")
# pos(x)        


# x = int(input("Write 1 number to divide "))
# y = int(input("Write 2 number that will divide "))

# def div(x,y):
#     z = x%y
#     if z == 0:
#         print("This is devisible ")
#     else:
#         print("This is not divisible ")

# div(x,y)


# x = int(input("Write ur age for voting"))

# def vote(x):
#     if x >= 18:
#         print(" U can vote")
#     else:
#         print("U can't vote")
# vote(x)


# x = int(input("Write  number1"))
# y = int(input("Write  number2"))
# z = int(input("Write  number3"))



# def slc(x,y,z):
#     print("The maximum value is ", max(x,y,z))

# slc(x,y,z)



# score = int(input("What is ur score "))

# if 0 <= score <= 100:
#     def scores(score):
#         if 90 <= score <= 100:
#             print("U have A score and u passed")
#         elif 80 <= score <= 89:
#             print("U have B score and u passed") 
#         elif 70 <= score <= 79:
#             print("U have C score and u passed")
#         elif 60 <= score <= 69:
#             print("U have D score and u passed")
#         else:
#             print("U have failde exam")
#     scores(score)
# else:
#     print("It's not acceptable score")


# letters = {"a", "b", "c"}
# numbers = {1, 2, 3}

# letters_and_numbers = letters.union(numbers)

# print(letters_and_numbers)


# bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
# bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}

# print(bundle_1.symmetric_difference(bundle_2))


# s = set("Hello everyone")
# print(s)


# l1=[1,2,3,4,5]
# print(list(set(l1)))


# s = set([1,2,3,4,5,6])
# print(s)


# S = {78, 11, 54, 95, 16, 36, 61, 77, 150, 122}
# print("\nSet Items:", S)

# sEven = 0
# sOdd = 0

# for num in S:
#     if num % 2 == 0:
#         sEven += 1
#     else:
#         sOdd += 1

# print("Total Even Numbers =", sEven)
# print("Total Odd Numbers =", sOdd)

# numbers = {8, 16, 32, 64}
# halved_numbers = set()

# while numbers:
#     for num in numbers:
#         halved_numbers.add(num / 2)
#     numbers.clear()

# print("\nHalved Numbers:", halved_numbers)



# NegativeSet = {6, -22, -33, 78, -88, 15, -55, -66, 17}
# print("\nNegative Set Items =", NegativeSet)
# print("The Negative Numbers are:")

# for num in NegativeSet:
#     if num < 0:
#         print(num)
#     else:
#         continue


# numbers = {8, 16, 32, 64}
# halved_numbers = set()

# while numbers:
#     for num in numbers:
#         halved_numbers.add(num / 2)
#     numbers.clear()

# print("\nHalved Numbers:", halved_numbers)



# a = input("What is ur name?")
# def name(a):
#     print("Hello,", a)
# name(a)



# a = int(input("Write the number"))
# def square(a):
#     s = a**2
#     print("Square of", a, "is", s )
# square(a)

# def find_max(numbers):
#     maximum = numbers[0]
    
#     for num in numbers:
#         if num > maximum:
#             maximum = num
    
#     print("Max:", maximum)

# find_max([3, 7, 2, 9, 4])



# def remove_duplicates(lst):
#     new_list = set(lst)
    
   
    
#     print("Without duplicates:", new_list)

# remove_duplicates(["1, ", ])

# def print_even():
#     for i in range(1, 51):
#         if i % 2 == 0:
#             print(i)

# print_even()


# def print_dictionary(dictionary):
#     for key in dictionary:
#         print(key, ":", dictionary[key])

# print_dictionary({"name": "Ali", "age": 18})


# def multiplication_table(n):
#     for i in range(1, 11):
#         print(n, "x", i, "=", n * i)

# multiplication_table(5)


# def fibonacci():
#     a = 0
#     b = 1
    
#     for i in range(10):
#         print(a)
#         temp = a
#         a = b
#         b = temp + b

# fibonacci()


# def longest_words(words):
#     max_len = 0
#     result = []

#     for w in words:
#         if len(w) > max_len:
#             max_len = len(w)
#             result = [w]          
#         elif len(w) == max_len:
#             result.append(w)      

#     return result

# x = input("Enter a sentence: ").lower().split()
# print(longest_words(x))  



# def find():
#     x = input("Enter a sentence: ")
#     y = input("Search the element from ur sentence: ")
#     a = x.lower().split()
#     b = y.lower().strip()
#     count = 0
#     for i in a:
#         if i == b:
#             count += 1
    
#     if count == 1:
#         print(f"There's no repeatable words!")
#     elif count == 0:
#         print(f"There's no repeatable words!")
#     else:
#         print(f"There are {count} of words reapated")

# find()



# def longest_word():
#     words = input("Something ").split()
#     return max(words, key=len)

# print(longest_word())


# def find_index(lst, value):
#     if value in lst:
#         return lst.index(value)
#     else:
#         return -1
# print(find_index([12,234,5,567,8,0], 5))


# restricted_number = 4
# for x in range(6):
#     if x % 2 == 0:



# mat = [[1,2], [3,4], [5,6]]
# b = []
# for row in mat:
#     for x in row:
#         if x%2 == 1:
#             b.append(x)
# print(b)


# b = [x for row in mat for x in row if x%2==1]
# print(b)

# third_even_odd = []
# for x in range(10):
#     if x%3==0:
#         if x%2==0:
#             third_even_odd.append("Even")
#         else:
#             third_even_odd.append("Odd")
# print(third_even_odd)


# third_even_odd = [x for x in range(10) if x%3==0 if x % 2 == 0],[x for x in range(10) if x%3==0 if x % 2 != 0]
# print(third_even_odd)



# numbers = int(input("Write the number: "))
# a = []
# power = str(numbers)
# for i in range(numbers):
    


# f = open("data.txt", "r")
# content = f.read()
# print(content)
# f.close()

# f = open("data.txt", "r")

# for line in f:
#     print(line)

# f.close()


# def count_words(filename):
#     f = open(filename, "r")
#     text = f.read()
#     words = text.split()
#     f.close()
#     return len(words)

# print(count_words("data.txt"))


# f = open("data.txt", "r")
# text = f.read()
# f.close()

# text = text.replace("Python", "Py")

# f = open("data.txt", "w")
# f.write(text)
# f.close()

# n = int(input(" a nuEntermber: "))

# for num in range(1, n + 1):
#     temp = num
#     digits = len(str(num))
#     total = 0

#     while temp > 0:
#         digit = temp % 10
#         total = total + digit ** digits
#         temp = temp // 10

#     if total == num:
#         print(num)

# def add(a,b):
#     return a+b
# print(add(2,4))

# print((lambda a,b: a+b)(2,4))

# def maximum(a, b):
#     return a if a > b else b

# print(maximum(4,5))

# print((lambda a,b: a if a > b else b)(4,5))



# def is_even(n):
#     return n % 2 == 0

# print(is_even(5))
# print((lambda n: n % 2 == 0)(5))



# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("Hello"))

# print((lambda s: s[::-1])("Hello"))

# def string_length(s):
#     return len(s)
# print(string_length("Hello my dear!"))


# print((lambda s: len(s))("Hello my dear!"))



# def is_palindrome(s):
#     return s == s[::-1]
# print(is_palindrome("lol"))

# print((lambda s: s== s[::-1])("lol"))



# def celsius_to_fahrenheit(c):
#     return (c * 9/5) + 32
# print(celsius_to_fahrenheit(90))

# print((lambda c: (c * 9/5) + 32)(90))


# def first_letter(word):
#     return word[0]

# print(first_letter("Hello"))

# print((lambda word: word[0])("Hello"))


# def multiply_list(lst):
#     return [x * 2 for x in lst]
# print(multiply_list("Hello"))

# print((lambda lst: [x * 2 for x in lst])("Hello"))


# def calculate_power(base, exponent):
#     return base ** exponent + (base * exponent) - (base / (exponent + 1))
# print(calculate_power(10,2))
# print((lambda base, exponent: base ** exponent + (base * exponent) - (base / (exponent + 1)))(10, 2))


# print((lambda a:  a % 2 == 0)(3))


# sentence = "python is very powerful language"
# words_upper = [word.upper() for word in sentence.split()]
# print(words_upper)

# sentence = "python is very powerful language"
# lengths = [len(word) for word in sentence.split()]
# print(lengths)

# text = "programming"
# vowels = [c for c in text if c in "aeiou"]
# print(vowels)

# words = ["level", "python", "madam", "hello", "racecar"]

# palindromes = [w for w in words if w == w[::-1]]

# print(len(palindromes))

# def count_palindromes(words):
#     return len([w for w in words if w == w[::-1]])
# print(count_palindromes(["level", "python", "madam", "hello", "racecar"]))



# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# r = set1.symmetric_difference(set2)
# print(r)

# my_set = {1, 2, 3, 4, 5}
# my_list = [2, 4]

# r = my_set - set(my_list)
# print(r)


# my_set = {{1,3}, {3, 4}, {5,6}}

# print([sum(x) for x in my_set])

# s1 = {1, 2, 3}
# s2 = {2, 4, 5}
# s3 = {3, 6, 7}

# r = s1^s2^s3
# print(r)

# s1 = {"hi", "python", "cat"}
# s2 = {"hi", "python", "dog"}

# r = s1&s2
# s = set()
# for i in  r:
#     if len(i)%2==0:
#         s.add(i)
# print(s)


# with open("data.txt","r") as n:
#     a = n.read().split()
# with open("output.txt", "r") as b:
#     c = b.read().split()

# d = set(a) - set(c)
# print(d)



# my_list = [1, 2, 2, 3, 3, 3, 4]
# seen = []
# duplicates = []
# for x in my_list:
#     if x in seen:
#         duplicates.append(x)
#     elif x in not in seen:
#         seen.append(x)
# print(set(duplicates))


# # matrix = [[1, 2], [3, 4]]

# # print([])

# def twice(lst):
#     freq = {}
    
#     for i in lst:
#         if i in freq:
#             freq[i] +=1
#         else:
#             freq[i]= 1
#     result = [x for x in lst if freq[x]==2]
#     return set(result)
# # test
# my_list = ["apple", "banana", "apple", "cherry", "banana", "mango", "mango", "mango"]
# print(twice(my_list))



# def words_once(para1, para2):
#     w1 = para1.split()
#     w2 = para2.split()
    
#     freq = {}
    
#     # count all words from both paragraphs
#     for w in w1:
#         if w in freq:
#             freq[w] += 1
#         else:
#             freq[w] = 1
    
#     for w in w2:
#         if w in freq:
#             freq[w] += 1
#         else:
#             freq[w] = 1
    
#     result = []
    
#     # check: appears in both AND total count = 2
#     for w in w1:
#         if w in w2 and freq[w] == 2 and w not in result:
#             result.append(w)
    
#     return result


# # test
# para1 = "the cat sat on the mat"
# para2 = "the dog sat on a log"

# print(words_once(para1, para2))



# my_set = {4, 9, 16, 25}
# root_squeare = set()
# for i in my_set:
#     root_squeare.add(round(i**0.5, 2))
# print(root_squeare)



# words = ["banana", "apple", "berry", "avocado", "cherry"]

# d = {}

# for w in words:
#     first = w[0]
    
#     if first in d:
#         d[first].append(w)
#     else:
#         d[first] = [w]

# print(d)





# def f(*a):
#     count = a[0]
   
#     for i in a:
#         if i == a[0]:
#             continue
#         count -= i
#     return count

# print(f(8,2,3,4,5,6,7))


# def f(*a, **b):
#     return "This is positional arguments:", a, "/n", "This is keyword arguments:", b
    
# print(f(1, 2, 3, x=4, y=5))


# coutry = {"name": "Courtney", "age": 30, "city": "New York"}

# def i(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# i(**coutry)


# a = ()
# for i in range(1,20):
#     a += (i,)

# def f(*a):
#     return a
# print(f(*a))


# a = ()
# for i in range(1,21):
#     a += (i,)

# def f(*a):
#     for i in a:
#         print(i)
# f(*a)




# def calculate_total_cost(*price, **kwargs):
#     a = sum(price)
#     b = sum(kwargs.values())
#     total = a + b
    
#     return total

# print(calculate_total_cost(100, 50, 75, apple=10, banana=5))



# def shop_list(*a, **kwargs):
#     print("Items to buy:")
#     for item, quantity in kwargs.items():
#         print(f"{item}: {quantity}")

# shop_list('apple', 'banana', 'milk', apple=5, banana=3, milk='2 liters')

# b = []
# a = str(input("Write the sentence: ")).split()
# for i in a:
#     if i.isalpha():
#         b += i
# print(b)

