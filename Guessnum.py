import random
while True:
    mynum = int(input("Number : "))
    v = random.randint(1, 20)
    if v == mynum :
        print("correct")
        break 
    else:
        print("Incorrect")    
