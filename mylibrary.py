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