marks = int(input("input the total marks out of 500: "))
avg = marks/5

if(avg==50):
    print("improvment needed")

elif(avg==60):
    print("can do better")

elif(avg==70):
    print("good")

elif(avg==80):
    print("V.good")

elif(avg==90):
    print("excellent")

elif(avg>90):
    print("brilliant")

else:
    print("enter marks as a multiple of 10")


