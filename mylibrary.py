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