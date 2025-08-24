#string manipution
#concatination
first_name= "pavan"
last_name = "Naik"
full_name = first_name + " " + last_name
print(f"{full_name}")

#repetition
message_1 = " warning! "*100
print(f"{message_1}")
message = "This is a warning!"
print(f"{message *100}")

#string methods

#upper()
note = "   stop!"
print(f"{note.upper()}")

#lower()
print(f"{note.lower()}")

#strip()  .using  for space erase
print(f"{note.strip()}")

#replace(old ,new) ..for replace strings
print(f"{message.replace("warning","error")}")

#replace(old, new) ..for replace strings
input = "This is a song"
print(f"{input.replace("song","dance")}")
a=input.replace("a","not")
print(a)

#multiline string
name = '''rahul said "hello'
         ramu said "hii"'''
print(name)

#repitions

print(len(message)) #lenght



