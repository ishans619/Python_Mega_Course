# user_entries = ['10', '19.1', '20']
# user_sum = [float(entries) for entries in user_entries]
#
# print(sum(user_sum))

temperatures = [10, 12, 14]

file = open("file.txt", 'w')

file.writelines(temperatures)