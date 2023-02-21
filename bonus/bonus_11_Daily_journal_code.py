# code to maintain a daily journal file of your's.

Date = input("Enter today's date: ")
mood = input("How would you rate your mood on a scale of 1 to 10 ?\n")
Thoughts = input("Let your thoughts flow for the day:\n")

with open(f"../Daily_Journal/{Date}.txt",'w') as file:
    file.write(mood + 2*"\n")
    file.write(Thoughts)