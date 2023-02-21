file = open('names.txt','r')
names = file.readlines()
file.close()

a = 5

while a<=5:
    name = input("enter your name: ")
    names.append(name)
    file = open('names.txt', 'w')
    names = file.writelines(names)
    file.close()


