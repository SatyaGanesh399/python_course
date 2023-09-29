# first program
print("hello world")

# second program
print("hello")
print("world")

# third program - can use end and sep
print("hello", end=" ")
print("world")

# variables
age = 25
weight = 71.5
isAdult = True
print(age, weight, isAdult)

# Taking inputs - input taken as string type
name = input("what is your name? ")
print(name)

age = input("whats your age? ")
print(type(age))
print(int(age))

# conversions
float()
bool()
str()

# Strings
name = "Satya Ganesh"
print(name)

state = """
Hello
this
is
a 
multiline
statement
"""
print(state)

# string methods
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name[5])
# negative indexing
print(name[-1])
# find function
print(name.find("n"))
print(name.find("goa"))
# replace
print(name.replace("a", "b"))
# subsctring
print(name[2:5])  # 2 is included but 5 is not included
print(name[:5])  # 0 to 4 comes
# isalpha, isnumeric and isalphanumeric
print(name.isalpha())
print(name.isnumeric())
print(name.isalnum())


# arthemetic operators
# + ,  -, *, /, //, ** and %
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 // 3)
print(2 ** 3)
print(2 % 3)

# augument operators
# += , -= and more
a = 2
a += 3
print(a)
a -= 3
print(a)

# comparison operators
# > , < , >=, <= and ==
print(2 > 3)
print(2 < 3)
print(2 >= 3)
print(2 <= 3)
print(2 == 3)

# logical operators
# and, or and not
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(not True)
print(not False)

# Conditional operators
# if, elif and else
a = 2
if a > 3:
    print("a is greater than 3")
elif a == 3:
    print("a is equal to 3")
else:
    print("a is less than 3")

# Loops in python
count = 1
while count <= 10:
    print(count * "*")
    count += 1

# list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[2:5])
print(numbers[2:])

list.insert("hello")
list.inser(0, "world")  # adds item at a desired position
list.append("funct")  # adds item at a last position
list.extend([1, 5, 7, 100])  # adds the list of items at the end
list.remove(5)  # removes the item from the list
list.pop()  # removes the last item from the list
list.reverse()  # reverses the list
list.sort()  # sorts the list
list.clear()  # clears the list
list.copy()  # copies the list -shallow copy not deep copy
print(sum(list))  # predefined function
print(min(list))  # predefined function
print(max(list))  # predefined function
print(list.count(5))  # predefined function
print(list.index(5))  # predefined function
print(sorted(list))  # only returns sorted list but doesnt change the original list

# for loop
for num in list:
    print(num)

# range
for num in range(1, 11):  # doesnt include 11
    print(num)
for num in range(1, 11, 2):  # 2 is step
    print(num)

# sets
list = [3, 2, 4, 6, 3, 4, 5]
myset = set(list)
print(myset)

for item in myset:
    print(item)  # printing thr items of set

myset.add(10)  # adds the 10 into the set
myset.update({10, 20, 30})  # adds multiple elements
# removes the 10 from the set - risky - if not there throws error
myset.remove(10)
myset.discard(10)  # removes the 10 from the set if present
myset.pop()  # removes the last item from the set
myset.clear()  # clears the set
print(myset)

set1 = set({2, 3, 4, 5})
set2 = set({1, 2, 3, 4, 5})

set3 = set1.union(set2)  # set1 | set2 same
set4 = set1.intersection(set2)  # set1 & set2 same
# set1 - set2 same prints set1 items which are not common but not set 2 items
set5 = set1.difference(set2)
set6 = set1.symmetric_difference(set2)  # set1 ^ set2 same
print(set3)
print(set4)
print(set5)

# tuple

a = 1, 2, 3, 4  # initilization
b = (1, 2, 3, 4)  # initilization
# initilization -  but mutable inside the elemets in list
c = tuple([5, 6, 7, ["hello", "world"]])
d = tuple(5, 6, 7, 8)  # initilization
print(type(a))
print(type(b))
print(a)
print(b)
print(a[0])
print(b[0])

del a  # deletes a tuple
print(b.count(1))  # frequency of 1
print(c.index(2))  # index of 2

print(3 in c)  # True or False

# dictionary

dic = {"name": "Satya", "age": 28}
print(dic)
print(dic["name"])
print(dic.values())
print(dic.keys())
print(dic.items())  # gives list of tuples(key, value)
print(dic.pop("age"))  # removes age key -value from dic
print(dic.clear())  # removes all items
