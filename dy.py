""""
is_failed=True
i=1 #attempt

while is_failed:
    print(f"try{i}")
    i+=1
"""
"""""
is_failed=True
i=1
while is_failed:
    print(f"try{i}")
    i+=1
    if i>100:
        break
        """
"""""
is_failed=True
i=0
while is_failed:
    if i%2!=0:
        i+=1
        continue
    print(f"attempt{i}")
    i+=1
    if i>100:
        break
        """
"""""
i=0
while i<=10:
    x=0
    while x<i:
        print("pablo",end="-")
        x+=1
    print("")

    i+=1
    """

"""
pin="1122"
input_pi=input("PIN>>")
if pin==input_pi:
    print("CORRECT")
else:
    print("INCORRECT")

"""

pin="2233"
while True:
    input_pin=input("PIN>>")
    if pin==input_pin:
        print("CORRECT")
        break
    else:
        print("INCORRECT")
