#operators

a= 10
a = a+100 #a += 100  shortform
#or
a += 100
print(a)

#comparison operators
x=10
y=20
print(f"{x==y}") # (x>y) , (x<y), (x!=y)

#logical operator and membership operator

c = "pavan"
c2 = "pavank"
print("a" in c) #membershipOperator
print(("k" in c2) and ("k" in c))#LogicalOperator
print(("k" in c2) or ("k" in c))