#doubling each number in a list
l=[1,2,3,4,5]
n=[]
for num in l:
    n.append(num*2)
print(n)

#printing food items in a list
b=["apple","banana","cherry"]
for items in b:
    print(f"i love {items}")

#looping through dictionary
#ex1
m={
    "fruit":"apple",
    "non_veg":"fish",
    "sugar":2
}
for l in m.values():
    print(f"{l} is a key in your dictionay")

#ex2 both keys and values
k={
    "fruit":"apple",
    "non_veg":"fish",
    "sugar":2
}
for name, value in k.items():
    print(f"{name}:{value}")



#accesing two list in a for loop
employee=["tony","peter","pablo"]
salary=[5000,6000,8000]
emp_salary={}
for num,emp in enumerate(employee):
    emp_salary[emp]=salary[num]
print(emp_salary)

#or
player=["rocky","pavan","manoj"]
score=[45,65,35]
players_score={}
for i in range(len(player)):
               players_score[player[i]]=score[i]
print(players_score)

#0
worker=["pablo","abhi","puni"]
work=["developer","tester","manager"]
worker_work={}
for i in range(1,len(worker)):
      worker_work[worker[i]]=work[i]
print(worker_work)

#list comprehension
#doubling each number in a list using list comprehension
l=[1,2,3,4,5,6]
dl=[item*2 for item in l]
print(dl)

#or
h=[x for x in range(1,10)]
x=[x**2 for x in h]
print(x)

#if
c=[y for y in range(1,10)]
d=[y**2 for y in c if y%2==0]
print(d)

#dictonary comprehension
my={"pavan","dinesh","pablo"}
my_n={name:len(name) for name in my}
print(my_n)



                    




