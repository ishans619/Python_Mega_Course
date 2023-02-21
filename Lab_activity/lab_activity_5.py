number = int(input("enter the number to be checked: "))
temp = number
sum = 0

while(number > 0):
    div = number%10
    sum = sum+div**3
    number = number//10

print(sum)
if(temp == sum):
    print("armstrong")

else:
    print("not armstrong")
print("ISHAN SHUKLA,21BCS7129")
