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

#Try ...excerpt
#All the code that should work goes inside the try.
#The error messages/instructions to handle any errors running the try code go inside the except.
myStuff = []

try:
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
# Try to find a file called 'Stuff.mine' and open it

except:
  print("ERROR: Unable to load")
# If the file can't be found, show the error instead of crashing the whole program

for row in myStuff:
  print(row)

#We can tell except what type of error(s) to look for. Exception (capital 'E') means 'every type'. I've captured the error type in the 'err' variable and printed it out to tell me what the error is. Here's a list of some built in except error codes.
myStuff = []

try:
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
# Try to find a file called 'Stuff.mine' and open it

except Exception as err:
  print("ERROR: Unable to load")
  print(err)


for row in myStuff:
  print(row)

#Traceback:
#We could even get rid of the 'err' variable entirely and print a traceback, which will show you the red error tracing you see when python crashes.

#I've created a 'debugMode' variable at the top of my code and put the traceback in an if inside the except.

#This lets me show/hide the tracebacks easily by setting debugMode to True/False:
debugMode = True
myStuff = []

try:
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
# Try to find a file called 'Stuff.mine' and open it

except Exception:
  print("ERROR: Unable to load")

  if debugMode:
    print(traceback)

for row in myStuff:
  print(row)

#CSV files:
# How to import CSV files
import csv # Imports the csv library

with open("January.csv") as file: 
  reader = csv.DictReader(file) # Treats the file as a dictionary 
  total = 0
  for row in reader: 
    print (row["Net Total"])
    total += float(row["Net Total"]) # Keeps a running total

print(f"Total: {total}") #Outputs

#The os library:
#listdir() will allow you to list all the files:
import os

print(os.listdir()) # Lists all the files in the current directory. Useful for checking that a file is in the folder we think it is.

files = os.listdir()
if "quickSave.txt" not in files:
  print("Error: Quick Save not found.")
#Checks if a file is in a directory and outputs an error if not.

#os.mkdir() creates a folder:
import os

os.mkdir("Hello") # Creates a folder called 'Hello'

#os.rename() takes 2 arguments: the file to rename and the new name.
import os

os.rename("myname.txt", "NEW.o")

#Recursion:
#Recursion is a type of program where you get a subroutine to call itself.

def factorial(value):
  if value == 1:
    return 1
    # This `if` provides the 'stop' condition for the program. Otherwise it would run forever.
  else:
    return value * factorial(value-1)
     # if we're not at the stop condition.

print(factorial(5))

#Timefunction:
datetime
import datetime

myDate = datetime.date(year=2022, month=12, day= 7)

print(myDate)

# This code outputs '2022-12-07'
#datetime.time -> returns a new data type - an actual date
datetime.time( year= any year, month= any month, day= any day)

#Asking For A Date:
import datetime

today = datetime.date.today()

print(today)

# This code outputs the current date from your computer's clock.

#Getting data input:
import datetime

day = int(input("Day: ")) # Get all input as numbers. We're not at text input for months yet.
month = int(input("Month: "))
year = int(input("Year: "))

date = datetime.date(year, month, day)

print(date)

#A common task in programs is to work out the difference between two dates, for example to calculate someone's age via timedelta()
import datetime

today = datetime.date.today() # Today's date

difference = datetime.timedelta(days=14) # The difference I want

newDate = today + difference # Add today to the delta difference to see the date in 14 days time.

print(newDate)

#If statements with days:
import datetime

today = datetime.date.today() # Today's date

holiday = datetime.date(year = 2022, month = 10, day = 30) # The date of my holiday

if holiday > today: # If my holiday is in the future
  print("Coming soon")
elif holiday < today: #If my holiday date has passed
  print("Hope you enjoyed it")
else: # If my holiday date is today
  print("HOLIDAY TIME!")

#Replit DB:
#Storing data:
#db[KeyName] = KeyValue :
from replit import db

db["test"] = "Hello there"

#Print all keys:
from replit import db

keys = db.keys()
print(keys)

#Print one key only:
from replit import db

value = db["test"]
print(value)

#Removing data/delete a key:
from replit import db

del db["test"]

#Accessing data by prefix:
from replit import db

#set up db:
db["login1"] = "david"
db["login2"] = "pamela"
db["login3"] = "sian"
db["login4"] = "ian"

#Search fall keys that start with "login"
matches = db.prefix("login")
print(matches)

#Keys and dictionaries:
#This example uses 'david' as the key, and a dictionary as the value. Look at how we can use this to store all of the user data in one key location
from replit import db

db["david"] = {"username": "dmorgan", "password":"baldy1"}

#List all the keys:
from replit import db

keys = db.keys()
print(keys)

#Access individual elements in the dictionary in the normal way:
from replit import db

value = db["david"]
print(value["password"])

#Looping Access:
from replit import db

keys = db.keys()
#Returns all the keys in the database

for key in keys:
  print(f"""{key}: {db[key]}""")
  #prints the key name and prints the key value


#Classes
#Let's create a template, known as a class. Our theme is animals. Our class will contain all the characteristics (think variables) that animals have in common.

#Remember that this is just a template. All the characteristics are set to 'None' in the template and we will customize these values when we use the template to create (instantiate) each animal. The values will be passed as arguments into the __init__ subroutine inside each animal object.

#We also want to create a subroutine called init (short for initialisation) which tells the class what to do when it is used to create each instance of an animal.

def__init_(self, list of arguments):
  code here

class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound
  # 'self' means 'this object'
  # This code sets the name, species and sound of each object to the arguments passed in when it is created (instantiated).

#Instanatiion
#nstantiation means 'use the template to create an object'. Like pressing the cutter into the dough to make a cookie.
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics
  def talk(self):
    print((f"{self.name} says {self.sound}")) 

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

##### THE NEW BIT #######

dog = animal("Brian", "Canine", "Woof") # Use the animal class to create a new object called 'dog' with the following parameters.

#Inheritance
#Inheritance means that we can take the template from animal and break it down into sub-classes that use all the attributes and methods from that class, but also add their own attributes.

#This is useful when we're thinking about animals as we can start breaking the animal kingdom apart by species.

#When I create the sub-class, I use the name of its parent class as a parameter. This means 'get all the features of animal and use them here too'.

#Here, I'm creating a sub-class of bird, which inherits from animal.

#I can then create the 'bird specific' features inside the bird sub-class.
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound
  
  def talk(self):
    print((f"{self.name} says {self.sound}")) 

##### The New Bit ##########

class bird(animal):
  color = None

  def __init__(self, color):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = "Green"

    # This automatically sets the information for each bird when it is created.


polly = bird() # Instantiates a new bird which gets it's details from the sub-class.

polly.talk() # polly uses the `talk()` method from the animal class

#TKinter library -> getting GUI
import tkinter as tk:
#Creates the window of the app:
window = tk.Tk()
#Set the title of the window:
window.title("Title of the window")
#Window size is a string in pixels width x height
window.geometry("300x300")
# here follows code to set up the app
# Label text at the top of the window below title:
hello = tk.Label(text="Hello World")
#Buttton below the Label:
button = tk.Button(text="Click me!")
button.pack()
#How to get button's to do things: via subroutines:
myButton = tk.Button( text= "Text to Show", command=Subroutine_to_run)
#No brackets needed on the subroutine name
#Place button into the window:
myButton.pack(side = tk.TOP)
#Creates a text box:
myText = tk.Text(Window_Name, height=1, width=25)
myText.pack(side=tk.TOP)
#Other options to place on TOP is BOTTOM, LEFT, or RIGHT or you can use the grid option. The grid option is laying a grid over the window:
myText = tk.Text(Window_Name, height=1, width=50).grid(row=1, column=2)
# Starts the app
tk.mainloop()




# This app uses the secret function of replit as environment variables
#Build a login system for two types of user.

#Your program should:

#    Have two types of user - admin and normal. Each should have their own username and password.
#    The admin user should be greeted with 'Hello admin'.
#    The normal user should be greeted with 'Hello normie'.

# This is the solution:

# The user and password is stored as a secret as a key(=user) and value(=password) pair


import os  # importing the os module

Admin_password = os.environ['admin']  # fetching admin password from environment variables
User_password = os.environ['dave']  # fetching dave's password from environment variables

username = input('Username > ').capitalize()  # getting username input and capitalizing
userPass = input("Password > ")  # getting password input

if username == 'Dave' and userPass == User_password:  # checking if username is Dave and password matches
  print("Wellcome Normy")  # printing welcome message for Dave
elif username == 'Admin' and userPass == Admin_password:  # checking if username is Admin and password matches
  print("Wellcome Admin")  # printing welcome message for Admin
else:
  print("Better luck next time")  # printing failure message for invalid credentials


# short programm with subroutine to collect username and password and another subroutine to perform the login action
from replit import db  # Importing the database from replit
import os, time, random  # Importing os for system operations, time for delays, and random for generating salts

# Function to add a new user to the database
def add_user():
  username = input("Username: >")  # Prompting for username
  password = input("Password: >")  # Prompting for password
  salt = random.randint(1,9999)  # Generating a random salt
  password = f"{password}{salt}"  # Appending salt to password
  password = hash(password)  # Hashing the password with salt
  if username in db:  # Checking if username already exists in database
    print("Username already in database")  # Informing user about existing username
    return
  else:  
    db[username]={"password": password, "salt":salt}  # Adding new user to database
  return

# Function for user login
def login():
  username = input("Username: >")  # Prompting for username
  password = input("Password: >")  # Prompting for password
  if username not in db.keys():  # Checking if user exists in database
    print("User does not exist.")
    print("Login not succssful")
    return
  password = f"{password}{db[username]['salt']}"  # Appending user's salt to entered password
  password = hash(password)  # Hashing the password with salt
  if password == db[username]["password"]:
    print("Login successful")  # Login success message
  else:
    print("Login not succssful")  # Login failure message
  return

# Main program loop handling user input and actions
try:
  while True:
    time.sleep(1)  # Adding a delay of one second
    os.system("clear")  # Clearing the console screen
    print("🌟Login System🌟")  # Printing the title of the system

    choice = input("1: Add User, 2: Login, 3: Terminate 4: Print Database>")

    if choice == "1":
      print("Choice 1")
      add_user()

    elif choice == "2":
      print("Choice 2")
      login()

    elif choice == "3":
      print("Program Terminated")

      break
    elif choice == "4":

      if not db.keys():
        print("Database is empty.")
      else:
          for key in db.keys():
            print(f"{key}: {db[key]}")
    else: 
      print("Wrong input")


except KeyboardInterrupt:
  print("\nProgram exited by user.")


# html chapter
# Each page constructed by a number of tags
#myWebPage.html
<html>
  <body>
    <p> Hi /<p>
  <body>
<html>
# In replit you have the feature of creating a file with the ".html" as ending. This page is supported by a couple replit features for html files The html page is then hosted on replit infrastructure and available from the Internet
 # Typical html structure is to wrap everything with a tag at the beginnin and at the end
#Starts the tag, everything after this point is in the tag
 <tagName>
 Stuff in the tag
</tagName>
 #Ends the tag. This stops the effect of the tag of any further code
 #HTML page example
<html>
#Starts the page
<head>
    # Hold the information that won't be visible
  <title>
  #What's goiong to be shown as the tab name

  </title>
  #Link to a style sheet in CSS with filename "style.css"
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

#body contains all the stuff that is visible
<body>

#Creates a heading with h1 largest heading and h6, the smallest
  <h1>This is a heading</h1> 
  <h2>This is a sub-heading</h2>

#Creates a normal text paragraph in standard fond and standard color. Each new paragraph needs new tags
   <p>
     This is normal text
   </p>

#To format this paragraph a class defintion with name ".blurb" is used from style.css sheet
   <p class="blurb">The continuation of the epic website showing the best of the bald bunch.</p>
#If you want to include images you need to drop the picture in the source code folder. Pictures must be of format .jpg. And there is no closing tag
#   <img src="picture.jpg" width="100" height="100">

#you can include arguments into the img like width and height and provide numbers like percantage or pixels
# you can add unordered lists with bullet points or ordered list with numbers
   #This is an unordered list
   <ul>
     # per each bullet point you need an opening and a closing li tag. Everything between these two tags is on one line 
     <li>
       bullet 1
       bullet 2
       bullet 3
     </li>
    # Here starts the the second bullet point
     <li>
       bullet 2
     </li>
     <li>
       bullet 3
     </li>
   </ul>

#This is an oderred list that starts with "1.".... and so on
   <ol>
     <li>
       bullet 1
       bullet 2
       bullet 3
     </li>
     <li>
       bullet 2
     </li>
     <li>
       bullet 3
     </li>
   </ol>

#Finally, we have the referencing to other web pages via the anker tag
#This is a link to a page in the same folder/repository. The text between the paragraph tag is shown on the webpage and linked to what is between the anchor tab.
  <p><a href=page2.html>Go to page 2</a></p>
</body>

 #Ends the page
</html>

#CSS style sheet example:

# There is a good tutorial on CSS in https://www.w3schools.com/css/default.asp/ */

# The structure is always like this:
#This will apply the style to all tags in the html with the Name "tagName" and followed by list of properties and their values

tagName {
  property: value;
}

*/


html, body {
  height: 100%; #/* Set the height of the html and body to 100% */
  width: 100%; #/* Set the width of the html and body to 100% */
  background-color: #e4e2e2;
  # Set the background color */
}

h1, h2{
  font-family: sans-serif; #/* Specify the font family */
  font-size: 24px; #/* Set the font size for h1 and h2 */
  color: blue; #/* Set the text color */
  background-color: #d3d345; #/* Set the background color for h1 and h2 */
  text-align:center; #/* Align the text to the center */
}

h2{
  font-size: 12px; #/* Set the font size for h2 */

}

p{
  font-family: sans-serif; #/* Specify the font family for paragraphs */
  font-size: 10px; #/* Set the font size for paragraphs */
  color: blue; #/* Set the text color for paragraphs */
  text-align:center; #/* Align the text to the center for paragraphs */

}

img{
  display: block; #/* Display images as block elements */
  margin-left: auto; #/* Center align images horizontally */
  margin-right: auto; #/* Center align images horizontally */
  width: 50%; #/* Set the width of images to 50% */

}

#/* This is a classe definition used to define properties in html file for a paragraph <p class"blurb"> test </p>*/
.blurb{
  font-style: italic; #/* Make the text italic */
  font-weight: bold; #/* Make the text bold */
}

# Flask Boiler Template to run a web app:
from flask import Flask # Imports the flask library

app = Flask(__name__) # Starts the Flask application. The 'app' variable is very important. We'll be using that later.


@app.route('/') # Tells the code what to do if we've gone to our web address with just a / after the URL
def index(): # Tells the code which webpage to show. This subroutine will display the 'Hello from Flask' page
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81) # This line should ALWAYS come last. It's the line that turns on the Flask server.

# Simple Flask app that opens a page and replaces the heading and shows it on screen
from flask import Flask  # Import Flask class

app = Flask(__name__)  # Create an instance of the Flask class

@app.route('/')  # Define the route for the main page

def index():  # Function to handle requests to the main page
  myName = "Olaf"  # Define a variable for the name to be used in the HTML page
  page = ""  # Initialize the variable to hold the HTML page content
  f = open("index.html", "r")  # Open the HTML file in read mode
  page = f.read()  # Read the contents of the file into the 'page' variable
  f.close()  # Close the HTML file
  page = page.replace("{name}", myName)  # Searches for the variable {name} in the html file and replances with variable "myName" 
  return page  # Return the modified HTML page

app.run(host='0.0.0.0', port=81)  # Run the Flask app on the specified host and port
# this the related index.html page
<!DOCTYPE html>   <!-- Document type declaration -->
<html> <!-- Root element of the HTML document -->
    <title>Olaf's Testpage</title> <!-- Title of the HTML document, shown in browser tab -->
    <body> <!-- Main content area of the HTML document -->
      <h1>Good Morning {name}</h1> <!-- Header element displaying a greeting message dynamically -->
    </body>   <!-- Closing tag for the body element -->
</html> <!-- Closing tag for the root HTML element -->

# Create template folder
# Add a html file "index.html"
# Add html file "cool_form.html"
# This is index.html:
<!doctype html>
<html>
<body>
    <p><a href="{{ url_for('cool_form') }}">Check out this cool form!</a></p>
</body>
</html>
# This cool_form.html
<!doctype html>
<html>
<body>
    <form method="post">
        <button type="submit">Do it!</button>
    </form>
</html>
# code from https://stackoverflow.com/questions/27539309/how-do-i-create-a-link-to-another-html-page

#url_for generates urls to routes defined in your application. There are no (or should probably not be any) raw html files being served, especially out of the templates folder. Each template should be something rendered by Jinja. Each location you want to display or post a form to should be handled and generated by a route on your application.

#In this case, you probably want to have one route to both render the form on GET and handle the form submit on POST.

from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('cool_form.html')


app.run(host='0.0.0.0', port=81)

## Simple example.html file that uses forms to collect user input
## you need to rename the form.html page into index.html page to run it in replit
<!DOCTYPE html><!-- Document type declaration -->
<html><!-- Root element -->

<head>

</head>

<body>
  Hello world <!-- Simple greeting text -->
  <form method="post" action="/login"> <!-- Form element -->
  # the method "post" sends data from the form to the server
  # it bundles everything that is in between this tagsin <form method="...." into a dictionary and sends it by the method to the page named in action
  # the entrie that are in between <form>.....</form> are collected and submitted as a dictionary
    <p>Username: <input type="text" name="username" required> </p> <!-- Username input field -->
# the <input type=" text, number, password,..." name="The name this will have in the dictionary" value="Default value". The field "required" tells that input must be entered is necessary to proceed
    <p>Email: <input type="Email" name="email"> </p> <!-- Email input field -->
      # the email input type is looking for an @ sign as input
    <p>Password: <input type="password" name="password"> </p> <!-- Password input field -->
      # the password input typ masks the data entry with ***** so nobody can see data 
    <input type="hidden" name="userID" value="232"> </p> <!-- Hidden user ID field -->
    <p>
      Fave Baldy: 
      <select name="baldies">
        <option value = "david">David</option>
        <option value = "jean luc">Jean Luc Picard</option>
        <option value = "yul">Yul Brynner</option>
      </select>
    </p>
    #above code is for a selection
    #<select name ="name of select box or tag">
    # <option value = "value for this selection ones selected"< The text to display </option>
    #</select>
    # The name of the select tag is what will be used in the dictionary as the key name
    # The value will be set to whichever of the options is selected when the form is submitted

    <button type="submit">Login</button> <!-- Submit button -->
      #this button type button type="submit to send a form, button for other uses">"The text you want to on your button"</button>
      # Submit buttons will take the contents of the form, turn it into a dictionary then follow the method and action of the form
  </form>

</body>

</html>

#This program collects data from a "form" section in "example.html" and sends it to a dictionary "form" via POST method and transfers data from the "form" section into the "form" dictionary via "request"-method
#Depending what has been selected as option value in example.html page the program will display a different message
  
from flask import Flask, request, render_template  # Import necessary modules from Flask

app = Flask(__name__)  # Create an instance of the Flask class

@app.route("/login", methods=["POST"])  # Define route for '/login' with POST method
#The example.html page has a "form"-section with a POST method that sends the data to the server. 
#and the "action="" attribute that points to the "@app.route("/login"...)

#The "@app.route "/login" is the URL that the server will listen for when a POST request is made to it.
def process():  # Define the function process to handle the '/login' route
  page = ""  # Initialize an empty string variable or an empty page
  form = request.form  # Get the form data from the POST request

  if form["baldies"] == "david":  # Check if the 'baldies' field in the form equals 'david'
    page += f"You're alright {form['username']}"  # Append a success message to the page variable
  else:
    page += f"You've picked wrong {form['username']}"  # Append a failure message to the page variable
  return page  # Return the final page and display the message


@app.route('/')  # Define route for the root URL
def index():  # Define the function index to handle the root URL
  return render_template('example.html')  # Render the 'example.html' template

app.run(host='0.0.0.0', port=81)  # Run the Flask application on host '0.0.0.0' and port 81


# GET vs POST
# GET is used to retrieve data from a server, while POST is used to send data to a server. 
# With post, the data transmitted is encrypted using the webpage's default method. So if the URL starts https, then it's encrypted using the secure hypertext transfer protocols encryption algorithm.

#This makes post a better choice for usernames, passwords and so on.

#With get, the data is sent as plaintext as part of the URL, so it's not good for data you want to keep secure. However it is useful for settings, locations or other things that you might want to be able to bookmark.
                
#It's not a matter of security. The HTTP protocol defines GET-type requests as being idempotent, while POSTs may have side effects. In plain English, that means that GET is used for viewing something, without changing it, while POST is used for changing something. For example, a search page should use GET, while a form that changes your password should use POST.

# This short script starts with a simple Flask application that has a single route "/" that returns a simple HTML page with a "Hello From Flask" message.
# If you add to the index route "/" an url that contains this string "language?lang=eng" then this url is used to define a route that will handle the "/language" route with method Get. After the "?" is the name of the parameter "lang" and the value "=eng" that will be passed to the route.
    
from flask import Flask, request  # Import the Flask framework and request module to handle web requests

app = Flask(__name__)  # Create an instance of Flask

@app.route('/language', methods=["GET"])  # Define a route for the '/language' endpoint that accepts GET requests
def lang():
  data = request.args  # Get the query parameters from the URL
  if data == {}:  # Check if no data was provided
    return "Nothing here"  # Return a message if there are no parameters
  if data["lang"] == "eng":  # Check if the 'lang' parameter is 'eng'
    return "Hello, and welcome to our website"  # Return a welcome message in English
  if data["lang"] == "wel":  # Check if the 'lang' parameter is 'wel'
    return "Helo, this is welsh"  # Return a welcome message in Welsh
        

@app.route('/')  # Define a route for the root URL
def index():
  return "Hello From Flask"  # Return a greeting message from Flask

app.run(host='0.0.0.0', port=81)  # Run the Flask application on all available IP addresses at port 81
#Next is ay 83