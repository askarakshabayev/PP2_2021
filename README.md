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
git status - status of the code
git add filename (git add .)
git diff filename (git diff)

