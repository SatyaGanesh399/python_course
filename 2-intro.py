"""
Data sructures are the way to store data in an efficient manner

2 types of  data structures
1. linear structure
2. nonlinear structure


Linear structures
1. Arrays
2. Linked lists
3. Stacks - LIFO - Last in first out  
4. Queues - FIFO - First in first out
5. Matrix - 2 Diemensional data structure


Nonlinear structures
1. Binary Tree
2. Heaps
3. Hash tables
4. Graphs
"""

"""
Python Specific Data Structures
1. Lists
2. Tuples
3. Dictionary
4. Set

Types of data structes in python
1. Builtin types - lists, dict, tuple, set
2. userDefined types - stack, queues, trees, linkedlist, graph...


LISTS:
1. replica of arraylists in java(dynamic size)
2. non homogenous - data need not be any specific type..  - can be numbers, strings, float

"""
List = [1, 2, "hello", 3.4]
print(List)

# Multi dimensionl lists

a = [["hello", "world"], ["1", "world"], ["2", "world"], ["3", "world"]]
print(a)
# length of list - len(list)
print(len(a))

# concept of negative indexing
# instead of writing list[len(list) - 3] we can write list[-3].. it is same thing

list = [1, 2, "hello", "new"]
print(list[-2])
print(list[-1])
print(list[-3])


"""
TUPLES
1. immutable

usecase 
1. days or dates or months which should not be changed
2. immutablity is necessary
"""

tuple = (1, 2, 3, 4)
print(tuple)
print(type(tuple))
print(tuple[0])

"""
DICTIONARY
1. unordered
2. non-homogeneous

usecase
1. key-value pair
2. immutablity is necessary
"""

dict1 = {1: "hello", 2: "world"}
print(dict1)
print(dict[1])
print(type(dict1))

# create a dictionary with inbuilt functions
dic = dict({1: "DSA", 2: "Programming Language"})
print(dic)
print(type(dic))

dic2 = dict([(1, "hey"), (2, "world")])
print(dic2)


"""
SETS
1. unordered, mutable
2. non-homogeneous
3. no duplicates are there in the sets
"""


set1 = {1, 2, 3, 4}
print(set1)

set2 = set()
print(set2)

set3 = set([1, 2, 3, 4, 4, 4, 4, 4])
print(set3)
