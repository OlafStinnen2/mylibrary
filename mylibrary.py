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

#append()
row = [items to be added to list, next variable,...]
list.append(row)

#2D Dictionanries
dictName[RowKeyName] =
        { KeyName  : Key Value,
          NextKeyName : Next Value
        }
#The key is the name of the beast, but the value is a whole new dictionary that contains the details of the beast.

#Each key:value pair in the dictionary is now a key that accesses a related dictionary. See prettyPrint function:
def prettyPrint():
  print()

  for key, value in clue.items():
    # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
    print(key, end=": ")
    for subKey, subValue in value.items():
      # (nested) `for` loop moves along every subkey and subvalue in each subDictionary.
      print(subKey, subValue, end=" | ")
    print()

# To access one item (=subdictionary), use two square brackets [] to see RowKeyName results
print(dictName["RowKeyName"])

# To access one subkey item (=subdictionary), use first [] to reference to SubKeyName with [] to get SubKeyVAlue
print(dictName["RowKeyName"][KeyName])

#Saving to files
#Creating a new file:
f = open( fileName, Mode)


#The variable (f): This is needed to allow your program to communicate to the file. Normally this would have a lovely meaningful name. However, you will need to type this variable name lots, and lots, and lots. So short is good. 'f' is short for 'file'.

#The file name (the first item in brackets, "savedFile.txt"): You MUST code this to match the filename EXACTLY and include the file extension.

#The 'w' (second item in brackets): This sets the permissions for the file. 'w' means 'write'. This means that if the file doesn't already exist, the program will create a new blank file with that file name. However, if it does already exist it will be overwritten with a blank file.

#Writing Data To File
f.write( Data to be put in the file)
# This will write to the file, each time it's called it will add to the bottom and can be called as many times you want

#The data should be a sring, ideally so cast it with str() if you get errors

#Until now, the data is still in the ram. Noting gets saved until we close the file via .close()
f = open("savedFile.txt", "w")
f.write("Hello there")
f.close()
#Prenventing Overwrite
#We're going to change the file permissions from 'w' to 'a+'.

#'a' means append - add to the end of the file.

#However, if the file doen't exist, then it will crash.

#'a+' means 'add to the end of the file, or create a new one if it doesn't exist'.

#To add it to a NEW line a the end fo the file,  I've used the \n new line character.

f = open("savedFile.txt", "a+")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()

#Reading from a file
f=open( filename, Mode)
#f is a variable that points to the copy of the file
#filename can be anything with any extension
#Mode for 'r' for read only
f = open("filenames.list", "r")
contents = f.read()
f.close()
# We need a variable 'contents' to store the contents of the file otherwise it will be descarded
#f.read() reads all of the content of the file as a string
#f.close closes the copy of the file and frees up our temporary memory

#Bringing everything in in one go is fine, but it would be much more useful to have it as separate items so we can examine it more easily.

#To do this, use the .split() function in the second to last line. This splits the string into a list of individual elements.
f = open("filenames.list", "r")
contents = f.read()
f.close()

contents = contents.split() #added split here

print(contents)
#myString.split() breaks a string up into a List, using newlines to create each row of the list

#eading all the data at once is fine, reading one item at a time works slightly differently.

#It uses the .readline() function.

#The code below reads one line from the file.

f = open("filenames.list","r")
contents = f.readline()
print(contents)

f.close()

#Looping through lines of a file:
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()

  if contents == "":
    break
  #The last line in the file will be a blank
  #We break the loop if the line read is a blank

  print(contents)
  # Moved the print after the break so it won't output the final blank line.

f.close()
#replit coach uses eval() function to read a list from a file as string "[1,2,3,,..]" with the eval() function converting the string into pyhton list. However, it is a bit dangerous to use eval() because it can run malicious code if used with an input function
myStuff = []

f = open("Stuff.mine","r")
myStuff = eval(f.read())
f.close()

for row in myStuff:
  print(row)