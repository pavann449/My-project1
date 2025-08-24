#Write a program to print numbers from 1 to 10 using a while loop.
num=True
i=1
while num:
    print(i)
    i+=1
    if i>10:
        break

#Write a program to print the multiplication table of 5 using a while loop.
i=1
while i<=10:
    print(f"5 x {i} = {5*i}")
    i+=1

#Write a program to print all even numbers between 1 and 50 using a while loop.

i=1
while i<=50:
    if i%2!=0:
        i+=1
        print(i)
        continue
    i+=1

#Write a program to take a number from the user and print its digits one by one using a while loop.
num=int(input("enter a number:"))
while num>0:
    digit=num%10
    print(digit)
    num//=10
"""""
Beginner Level

Write a program to print numbers from 1 to 10 using a while loop.

Write a program to print the multiplication table of 5 using a while loop.

Write a program to print all even numbers between 1 and 50 using a while loop.

Write a program to take a number from the user and print its digits one by one using a while loop.

Intermediate Level
5. Write a program that takes a number from the user and prints its factorial using a while loop.
6. Write a program to reverse a given number using a while loop.
7. Write a program to find the sum of digits of a given number using a while loop.
8. Write a program to check if a given number is a palindrome using a while loop.

Advanced Level
9. Write a program that asks for numbers repeatedly until the user enters 0, then prints the sum of all numbers entered.
10. Write a program to generate the Fibonacci series up to n terms using a while loop.
11. Write a program to keep asking the user for a password until they enter the correct one.
12. Write a program to count how many vowels are in a given string using a while loop
"""
#5. Write a program that takes a number from the user and prints its factorial using a while loop.
num=int(input("enter number:"))
fact=1
i=1
while i<=num:
    fact*=i
    i+=1
print(f"factorial of {num} is {fact}")