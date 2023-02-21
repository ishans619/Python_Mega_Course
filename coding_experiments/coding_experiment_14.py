# file = open('a.txt','r')
# a = file.readlines()
# file.close
# file = open('b.txt','r')
# b = file.readlines()
# file.close
# file = open('c.txt','r')
# c = file.readlines()
# file.close
# print(a)
# print(b)
# print(c)
#

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)