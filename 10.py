name=input("enter:")
vowels="aeiouAEIOU"
count=0
for char in name:
    if char in vowels:
        count+=1
print(f"Number of vowels in '{name}' is {count}")