# ...existing code...
#6. Write a program to reverse a given number using a while loop.
num = int(input("Enter a number to reverse: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(f"Reversed number is {rev}")
# ...existing code...12

num=int(input("enter a number:"))
while num>0:
    digit=num%10
    print(digit)
    num//=10