#My Library
# "import getpass" getpass is a utility to get passwords
import getpass                                                                       
p=getpass.getpass("Enter the Password:")
print(p)

# "while: True loop with break and continue
while True:
  lyrics = input("do (d) or not to do (n) or break (b) > ").lower()
  if lyrics == "d":
    print("Your are in the do path")
  elif lyrics == "n":
    print("you are in the not to do path")
  elif lyrics == "b":
    print("you are in the break path")
    break
  else:
    continue
    
# for loop
#range(stop: int)

#range(stop) -> range object range(start, stop[, step]) -> range object

#Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement).

Start = int(input("Start at: "))
EndBefore = int(input("End before: "))
Increment = int(input("Increment by: "))

for i in range(Start, EndBefore, Increment):
    print(i)


# for loop and while loop doing the same
for counter in range(10):
  print(counter)

counter = 0
while counter < 10:
  print(counter)
  counter += 1

# How to generate random numbers
import random
myNumber = random.randint(1,100)
print(myNumber)

# Create a subroutine:
# def subrouting_name(arguments):
  # run this code

def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

for i in range(100):
  rollDice()

# Subroutine with return command
#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
  return pin

pinPicker(4) #4 means we want 4 random numbers

# Adding os.system to clear screen
import os
print("Welcome")
os.system("clear")

# Adding time library to pause e.g. showing screen for 1 seconds until it is cleared
import time
time.sleep(1)
os.system("clear")

# print() patterns:
# print( VarName, end=" ")
# VarName: Normal code to be printed
# end=" ": Code to be printed at the end of the the print statement
#new line
for i in range(0, 100):
  print(i, end="\n")

#tab indent
for i in range(0, 100):
  print(i, end="\t")

#vertical tab
for i in range(0, 100):
  print(i, end="\v")

# print( VarName, sep=" ")
# VarName: Normal code to be printed
# sep=" ": Code to be printed between the arguments
print('Hello', 'World', sep='-')
print('Python', 'Programming', sep=' -> ')

# printing colors
def colorChange(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

# lists:
for NewVariable in ListName:
  print(NewVariable)
  
#or using the list index:
for NewVariable in range(len(ListName(ListName)):
  print(ListName[NewVariable])
  
#NewVariable creates a new variable
#ListName uses this list to move through
#RepeatThisCode is repeating all code, changing the variable to the next value in the list when it starts again
#List Example:
timetable = ["Computer Science", "Math", "English", "Art", "Watch TV"]
for lesson in timetable:
  print(lesson)

#Lists start couting with item with 0, next item is then 1

#This creates a blank list:
ListName=[]
# This function is used to append an item to to the list List.Name
ListName.append(item)
#Viceversa this function is ued to remove an an time from list ListName. But you can remove one item at a time only
ListName.remove(item)

#String Manipulation

string.lower() = all letters are lower case
string.upper() = all letters are upper case
string.title() = capital letter for the first letter of every word
string.capitalize() = capital letter for the first letter of only the first word
Adding .strip() then string.lower().strip() removes any spaces on either side of the word.

#String Slicing
String[start_pos:end_pos:step]
#The slicing starts with the start_pos index (included) and ends at end_pos index (excluded). The step parameter is used to specify the steps to take from start to end index.

#Reverse a String using Slicing
ReverseString = String[::-1]

#Split a string:
#split lets us split a string into a list of individual words by separating it at the space characters.
String.split()

# If the letters that represent the rainbow colors are in my sentence (=list), they will print out in color:
def colorChange(color):
  if color=="r":
    print("\033[31m", end="")
  elif color==" ":
    print("\033[0m", end="")
  elif color=="b":
    print("\033[34m", end="")
  elif color=="y":
    print("\033[33m", end="")
  elif color == "g":
    print("\033[32m", end="")
  elif color == "p":
    print("\033[35m", end="")

sentence = input("What sentence do you want rainbow-izing?: ")
for letter in sentence:
  colorChange(letter.lower())
  print(letter, end="")
print()

#Dictionaries:
#Dictionary items are ordered, changeable, and does not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). A colon (:) separates each key from its associated value:
d = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}

myUser = {
      "name": "David", 
      "age": 128
}
#To output (print) from a dictionary, we can use the key instead of the index. Note that we still use square brackets for accessing items (ex: ["name"]).
print(myUser["name"])

#You can use the = syntax to change key values. 
dictName[KeyName] = KeyValue

#Using a for loop, like we would with a list, will output the values, but not the keys. 
for i in myDictionary:
  print(myDictionary[i])

#This loop uses the .values() method, which can be run on a data type. We still only get the value, and not the key.
for value in myDictionary.values():
  print(value)

#Here's a loop that will output both key and value.
#The .items() function returns the key name and value. 
for name,value in myDictionary.items():
  print(f"{name}:{value}")

#How to iterate through dictionaries look here https://realpython.com/iterate-through-dictionary-python/

#Tables as two dimensional lists:
#Tables are two-dimensional data structures where we can store data both vertically and horizontally.

#Usually this means that vertical data is used for fields (one category - name, ID, favorite biscuit, etc.) and horizontal data is used for records (all the data for each category).
#Here, we will do row index first and then the column index.
ListName[RowIndex][ColumnIndex]
my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]
#Each new list has its own set of square brackets and is separated by a comma. This layout of code is nice to help us visualise the 2D list a a table

#printing 2 lists:
#Printing the entire table:
print(my2DList)

#Printing the first row:
print(my2DList[0])
# This code outputs ['Johnny', 21, 'Mac'].

#printing a single piece of data:
print(my2DList[1][2])
# This code outputs 'PC'. It's Sian's computing preferene from list 1 (first square bracket), item 2 (second square bracket)
