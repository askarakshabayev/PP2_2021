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

