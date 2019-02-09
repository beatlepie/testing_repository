import random

#Generates a random password
#1-	Must be over 10 characters long
#2-	Must be under 24 characters long
#3-	Must contains at least 1 uppercase and 1 lower case letter
#4-	Must contains at least 1 number
#5-	Must contains at least one of these special characters -|@.,?/!~#%^&*(){}[]\=*

#23 special characters
special = ["-", "|", "@", ".", ",", "?", "/", "!", "~", "#", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]", "\"", "=", "*"]
chararray = []
current = 0
length = random.randint(11, 23)
req = [False, False, False, False]

#this initializes the length of the random password
for i in range(length):
    current = random.randint(0, 85)
    if(current > 9):
        if(current > 36):
            if(current > 63):
                #special characters
                chararray.append(special[current - 63])
                req[2] = True
            #small characters
            chararray.append(str(chr(current + 60)))
            req[1] = True
        #capital characters
        chararray.append(str(chr(current + 55)))
        req[0] = True
    else:
        #numbers
        chararray.append(str(current))
        req[3] = True
    
#In case there are passwords that do not fit the critaria
while(True):
    if(False not in req):
        break
    if(not req[0]):
        chararray[randint(0, length)] = str(chr(random.randint[65,90]))
        req[0] = True
    if(not req[1]):
        chararray[randint(0, length)] = str(chr(random.randint[97,112]))
        req[1] = True
    if(not req[2]):
        chararray[randint(0, length)] = str(chr(special[random.randint(0,23)]))
        req[2] = True
    if(not req[3]):
        chararray[randint(0, length)] = str(random.randint[0,9])
        req[3] = True

        

print (length)
for i in chararray:
    print(i, end='')
