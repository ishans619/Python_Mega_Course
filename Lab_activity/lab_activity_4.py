number = int(input("enter the number to be checked: "))
temp = number
rev = 0

while(number>0):
    div = number%10
    rev = rev*10+div
    number = number//10

print(rev)
if(temp == rev):
    print("Palindrome")
else:
    print("Not Palindrome")
print("ISHAN SHUKLA,21BCS7129")



