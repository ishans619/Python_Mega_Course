member = input("Add a new member: ")
file = open('members.txt','r')
members = file.readlines()
print(members)
file.close()

members.append(member)

file = open('members.txt','w')
members = file.writelines(members)
file.close()


