#Password manager programm
#the programm creates and saves usernames and passwords
#23/02/21

name= ""
age= ""

print("Welcome to Password Manager!!")
print("If you are 13 or older, you can store access details")
name = input("What is your name?: ")
age = int(input("How old are you?: "))

print("Hello", name)

if age < 12:
  print("Sorry, you do not qualify to open an account")

elif age > 12: 
  print("Choose a mode by entering the number: ")
  mode = input("        1: Add passwords  2:View passwords  3: Exit")  
