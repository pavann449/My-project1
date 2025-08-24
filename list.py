""" 
items = ["bru", "sugar", "milk", "oil"]



#append
items.append("cocanut")
print(items) # add element

#remove
items.remove("sugar")
print(items)

#insert
items.insert(1, "spoon")
print(items)

#changing specific element
items [0] ="cofee powder"
print(items)

#LICING THE LIST
l=[100,200,600,400,500,700,800]
print(l[0::2])

#lenght of iteme
print(len(l))

#sorted items
print(sorted(l))
#sum
print(sum(l))

#COMMOM METHODS
#index lement
fruits=["apple","banana","orange"]
print(fruits.index("banana"))
#count element
num=[1,2,1,4,1,5]
print(num.count(1))

#reverse item
num.reverse()
print(num)

"""
list=[1,2,5,6,3,7,8]
print(list[0:8])

non=list((1,66,"tuple",76))
print(non)
