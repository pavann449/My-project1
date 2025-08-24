"""
Simple Greeting Program: Write a Python program that asks the user for their name and age, then prints a personalized greeting message. Use both the + operator and f-strings for output.

Example:

Enter your name: Alice
Enter your age: 25
Output: Hello, Alice! You are 25 years old.
"""

name=input("Enter your name:")
age=int(input("enter your age:"))
print(f"{"hello, " + name + "! you are " +str(age) + " years old"}")

""" 2.String Manipulation Exercise: Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.
Example:

Input: "   Python is awesome!   "
Output:
Uppercase: "PYTHON IS AWESOME!"
Lowercase: "python is awesome!"
Replaced: "___Python_is_awesome!___"
Stripped: "Python is awesome!"
"""
data=input("enter a string:")
print(f"{data.upper()}")
print(f"{data.lower()}")
print(f"{data.strip()}")
print(f"{data.replace("a" , "not")}")

""" 3.Escape Sequence Practice: Write a Python program that uses escape sequences to print the following output:

Example:

Hello
    World
This is a backslash: \
"""
pavan= "what \nabout \n\ttoday"
input=input("This is a backslash:")
print(f"{pavan}")

