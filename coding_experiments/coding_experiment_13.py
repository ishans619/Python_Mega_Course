filenames = ["first.txt","second.txt","third.txt","fourth.txt","fifth.txt"]
contents = ["Hello","Hello","Hello","Hello","Hello"]

for content, filename in zip(contents,filenames):
    file = open(f"../files/{filename}",'w')
    file.write(content)
    file.close()

