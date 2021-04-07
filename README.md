## Week 10
Ball Example 

keys = filter(lambda x: 'K_' in x, dir(pygame))

# pygame.key.get_pressed()
# pressed = pygame.key.get_pressed()
# pressed[pygame.K_UP]

# Surface

Working with Images
Music and Sound Effects
Geometric Drawing
Fonts and Text
More on Input

## Week 9
virtualenv
pip install virtualenv
python3 -m venv env
source path_to_env/bin/activate
pip install pygame
--------------------------------
import pygame

size = width, height = (400, 300)
screen = pygame.display.set_mode(size)
pygame.init()


def draw():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!", 1, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0),
                     (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
----------------------------------



## Week 6
abs()
x = abs(-7.25)

mylist = [True, True, True]
x = all(mylist)


-----------------------------
any
mylist = [False, True, False]
x = any(mylist)

# True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
print(any(l))

# False since both are False
l = [0, False]
print(any(l))

# True since 5 is true
l = [0, False, 5]
print(any(l))

# False since iterable is empty
l = []
print(any(l))

# 0 is False
d = {0: 'False'}
print(any(d))

# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))

# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))

# iterable is empty
d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))


numbers = [1, 3, 5, 7]

def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(any(is_even(number) for number in numbers))
-----------------------------
callable
def z():
    print("Hello world")

def f(x):
    if callable(x):
        x()
    else:
        print(x)

f(z)
f(5)

# x = 5
# print(callable(x))

# def testFunction():
#   print("Test")

# y = testFunction
# y()
# print(callable(y))
-----------------------------
x = bin(36)

bool()
The object is empty, like [], (), {}
The object is False
The object is 0
The object is None
-----------------------------
x = chr(97)
-----------------------------
compile(source, filename, mode, flag, dont_inherit, optimize)
x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x)
-----------------------------
x = divmod(5, 2)
-----------------------------
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))

empty = dict()
print('empty =', empty)
print(type(empty))

Using iterable
# keyword argument is not passed
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)

# keyword argument is also passed
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)

# zip() creates an iterable in Python 3
numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbers3 =',numbers3)

Using mapping
numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =',numbers1)

# you don't need to use dict() in above code
numbers2 = {'x': 4, 'y': 5}
print('numbers2 =',numbers2)

# keyword argument is also passed
numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =',numbers3)

-----------------------------

enumerate(iterable, start=0)
Example 1
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))


Example 2
grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)
-----------------------------
filter(function, iterable)
# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, letters)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)

Example 2
# random list
randomList = [1, 'a', 0, False, True, '0']

filteredList = filter(None, randomList)

print('The filtered elements are:')
for element in filteredList:
    print(element)
-----------------------------
format(value[, format_spec])
# d, f and b are type

# integer
print(format(123, "d"))

# float arguments
print(format(123.4567898, "f"))

# binary format
print(format(12, "b"))
x = format(255, 'x')
-----------------------------
frozenset([iterable])
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())

# frozensets are immutable
fSet.add('v')

Example 2
# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print(C)

# union
print(A.union(B))  # Output: frozenset({1, 2, 3, 4, 5, 6})

# intersection
print(A.intersection(B))  # Output: frozenset({3, 4})

# difference
print(A.difference(B))  # Output: frozenset({1, 2})

# symmetric_difference
print(A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})
-----------------------------
try except
-----------------------------
dir
class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))
-----------------------------
eval
x = 'print(55)'
eval(x)
-----------------------------
getatr
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'age')
-----------------------------
hasatr
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = hasattr(Person, 'age')
-----------------------------
setatr
class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)
-----------------------------
x = isinstance(5, int)
x = isinstance("Hello", (float, int, str, list, dict, tuple))

class myObj:
  name = "John"

y = myObj()

x = isinstance(y, myObj)
-----------------------------
iter
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))
-----------------------------
map(function, iterables)
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))
-----------------------------
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
-----------------------------
max, min
x = max("Mike", "John", "Vicky")
a = (1, 5, 3, 9)
x = max(a)
-----------------------------
open
f = open("demofile.txt", "r")
print(f.read())
-----------------------------
pow(x, y)
x = pow(4, 3)
x = pow(4, 3, 5) # Return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5):
-----------------------------
range(start, stop, step)
-----------------------------
reversed
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)
-----------------------------
slice(start, end, step)
# Create a tuple and a slice object. Use the slice object to get only the two first items of the tuple:
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])
x = slice(3, 5)
print(a[x])
x = slice(0, 8, 3)
print(a[x])
-----------------------------
sorted
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)
-----------------------------
str
-----------------------------
sum
a = (1, 2, 3, 4, 5)
x = sum(a)

a = (1, 2, 3, 4, 5)
x = sum(a, 7)



## Week 5
1. Working with csv
2. Module example (how to create setup file and install, virtual env)
  from setuptools import setup, find_packages
  setup(name='pip_lib_name', version='1.0', packages=find_packages())
3. working with files (open method read - r, append - a, write - w)
4. working with directories
4.1 os module


## Week 4
regex
. - Один любой символ, кроме новой строки \n. (h.l.o -> hello, hillo, halbo)
\d - цифра (BD\d\d -> BD02, BD13)
\D - Любой символ, кроме цифры (B\D\d. -> BA5l, BF25)
\w - Любой символ (\w\w\w -> 123, a3b, a_!)
\W	Любая не-буква, не-цифра и не подчёркивание
[..] - Один из символов в скобках, а также любой символ из диапазона a-b [0-9][0-9A-Fa-f] -> 12, 1F, 4B
[^aqz][0-9] a6 z9 b8
[^..] - Любой символ, кроме перечисленных 
\b	- Начало или конец слова (слева пусто или не-буква, справа буква и наоборот). В отличие от предыдущих соответствует позиции, а не символу \bвал вал, перевал, Перевалка
^	Starts with
$	Ends with
{}	Exactly the specified number of occurrences
{n}	Ровно n повторений (\d{4})
{m,n}	От m до n повторений включительно (\d{2,4})
{m,}	Не менее m повторений	\d{3,}
{,n}	Не более n повторений
?	Ноль или одно вхождение, синоним {0,1}
*	Ноль или более, синоним {0,}
+	Одно или более, синоним {1,}

|	Either or ([0-9]|[a-z])
()	Capture and group
\b	Returns a match where the specified characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")


\d{5} - цифры ровно 5 раз
\d\d/\d\d/\d{4} - дата в формате ДД/ММ/ГГГГ (но есть исключения)
\d{2}:\d{2}:\d{2} - Selecting time with format: 14:56:10
[-+]?\d+ -- число -1, 74, 00012
            [-+]? — либо -, либо +, либо пусто
            \d+ — последовательность из 1 или более цифр
[0-9]+ - все числа
\w+stan Kazakhstan, Kyrgyzstan, Uzbekistan
(\+7|8)\(?\d{3}\)?-?\d{3}-\d{2}-\d{2} - +7707-123-11-22  ----- +7(707)123-11-22 ---- 8(707)123-11-22
[a-z]+@[a-z]+\.[a-z]{2,5} - asd@gmail.com
[a-z0-9_]+@[a-z]+\.[a-z]{2,5} - asd3_asd@gmail.com
[A-Za-z0-9_]+\.?[A-Za-z0-9_]+@[a-z]+\.[a-z]{2,4}  - askar.akshabayev@gmail.com
[\w]+\.?[\w]+@[\w]+\.[\w]{2,4}  - askar.akshabayev@gmail.com



## Week 3
# What is Lambda function? (A lambda function can take any number of arguments, but can only have one expression.)
# Function declaration with lambda (anonymous function inside another function)
# Doubler / Tripler examples
    def f(n):
        return lambda a: a * n

    doubler = f(2)
    triple = f(3)

    print(doubler(5))
    print(doubler(6))

    print(triple(5))
    print(triple(6))

# only even numbers from a list (using filter) 
# only prime numbers from a list (using filter)
# double all elements in list (using map)
  --------------------------------------------
# What is class?
# OOP
# Class object
# Init function - constructor
# Object methods
# Self parameter
 
# What is class Inheritance?
# Parent class / Child class
# Calling parent class init function 
# super expression
 
# What is iterator?
# Iterator vs Iterable
# iter(), next() - for list, for string
# Example 1
t = (10, 2, 8, 5)
it = iter(t)

print(next(t))
print(next(t))
print(next(t))

# Example 2 (strings are also iterable objects)
s = "abcd"
it = iter(s)
print(next(it))

# Simple loops over containers
# Own iterator class: iter, next methods
class MyNumber:
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        x = self.x
        self.x += 1
        return x

n = MyNumber()

it = iter(n)

print(next(it))
print(next(it))
# StopIteration
 
# What is Generator?
The difference is that while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.
# Generator function
# Generator object
# Fibonacci

# What is Scope?
# Local scope
# Global scope
# Global keyword
 
# What is module?
# Alias while importing
# Import from module
 ◦ 
# Python Date
# Creating date object
# strftime method
 ◦ 
# Python Math functions
# min, max, pow, abs
# math module - sqrt, floor, ceil
 ◦ 
# What is JSON?
# Converting objects to JSON and vice-versa

## Week 2
Functions 
1. Function definition
2. function with arguments
3. Arbitrary Arguments, *args
4. Keyword Arguments
5. Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
------------------------------------------------
6. multiple return values
7. Recursion
------------------------------------------------
Collections:
List:
1. list example
2. element of the list and negative index
3. range
4. list comprehension 
[x ** 2 for x in range(1, 20)]
??[x+1 if x >= 45 else x+5 for x in l]
------------------------------------------------
Tuple
mytuple = ("apple", "banana", "cherry")
tuple length
Create Tuple With One Item
thistuple = ("apple",)

Example 1:
list1 = ["Almas", "Aidar", "Zhanel", "Madiyar"]
list2 = [18, 23, 34, 25]
list3 = [(list1[i], list2[i]) for i in range(0, len(list1))]

Example 2:
# x = 1
# y = 2
# z = 3
# a = 4

(x, y, z, a) = (1, 2, 3, 4)

(one, two) = range(1, 3)

Set
set_example = {"apple", "banana", "cherry"}
set_example = {"abc", 34, True, 40, "male"}

# list is ORDERED
my_list = [10, 10, 10, 1, 1, 1, 2]
my_set = set(my_list)
print(my_set)
------------------------------------------------
add element to set
------------------------------------------------
update with multiple value
my_set.update({10, 1, -4})
------------------------------------------------
my_set_2.discard(-10000)
------------------------------------------------
discard, remove
------------------------------------------------
A.union(B)
------------------------------------------------
A.intersection(B)
------------------------------------------------
A.difference(B) # A - B


Dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
Examples:
1. Create a function that collects only values with even index from a given list
2. Create a function that mutates elements to square after given index. Elements before given index do not change.
3. 



## Week 1
1. Syllabus, assistants
2. Midterm, Endterm, Project, Final Exam information
3. Tools (IDE, interpreter, version of python)
3. compilers vs interpreters (c++, java, python, javascript)
4. python --version
5. how to execute python program (show print example)
6. print("hello world") (using shell and using file) 
7. Python Indentation (example with if, different count of spaces - error)
8. Python comments
------------------------------------
9. Python variables
x = 5
y = "John"
print(x)
print(y)
------------------------------------
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)    
------------------------------------
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
------------------------------------
x = 5
y = "John"
print(type(x))
print(type(y))
------------------------------------
x = "John"
# is the same as
x = 'John'
------------------------------------
Case sensitive 
a = 4
A = "Sally"
#A will not overwrite a
------------------------------------
Variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
------------------------------------
Camel Case
myVariableName = "John"
Snake Case
my_variable_name = "John"
------------------------------------
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
------------------------------------
x = y = z = "Orange"
print(x)
print(y)
print(z)
------------------------------------
unpack collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
------------------------------------
Concatinating strings
x = "Python is "
y = "awesome"
z =  x + y
print(z)
------------------------------------
Data types
str, int, float, bool
list, tuple, range, dict, set, frozenset, map etc.
------------------------------------
Python casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
------------------------------------
Python string
'string', "string"

""" multiple string """

Strings are Arrays
a = "Hello, World!"
print(a[1])
------------------------------------
Looping through a String
for x in "banana":
  print(x)
------------------------------------
String length
a = "Hello, World!"
print(len(a))
------------------------------------
Check string
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)
------------------------------------
Slicing
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
------------------------------------
Modify string
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))
------------------------------------
format string
"hello world {}".format(5)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
------------------------------------
string methonds
count()	Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")

endswith()	Returns true if the string ends with the specified value

find(string, start_position=0)	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

format()	Formats specified values in a string
------------------------------------
Examples:
------------------------------------
a = '5'
b = int(a)
a = str(b)
print(b)
------------------------------------
import math
print(math.pi)
print(math.factorial(5))
------------------------------------
a = int(input())
b = int(input())
c = a + b
print(c)
------------------------------------
a, b, c = input().split()
print(2 ** int(a), 2 ** int(b), 2 ** int(c))
------------------------------------
a = float(input())
print("Hello, {}".format(a))
------------------------------------
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2:
    print("Yes")
else:
    print("No")
------------------------------------
Python Operators
+, -, *, /, %, **, //
+=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
==, !=, >, <, >=, <=
and, or, not
is, is not
in, not in
&, |, ^, ~, <<, >>
------------------------------------
if else
------------------------------------
while loop (while with else)
break, continue
------------------------------------
for loop
------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)  
------------------------------------
for x in "banana":
  print(x)
------------------------------------
range function
for x in range(6):
  print(x)
------------------------------------
for x in range(2, 6):
  print(x)
------------------------------------
for x in range(2, 30, 3):
  print(x)
------------------------------------
for x in range(6):
  print(x)
else:
  print("Finally finished!")
------------------------------------
nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
------------------------------------
python arrays (list)
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
cars[0] = "Toyota"
t = len(cars)
for x in cars:
  print(x)

cars.append("Honda")
cars.pop(1)

clear()
------------------------------------
count()
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
------------------------------------
extend()
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
------------------------------------
index()
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
------------------------------------
insert()
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
------------------------------------
remove()
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
------------------------------------
sort()
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
------------------------------------
Examples:
read array from input
------------------------------------
arr = [1] * (10)
------------------------------------
git example
------------------------------------
git init
git status - status of the code
git add filename (git add .)
git diff filename (git diff)
git commit -m "comment"
git remote add origin link_to_git_repository
git push origin master (name of branch)
git pull origin master 
git log

