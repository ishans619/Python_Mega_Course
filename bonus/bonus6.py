contents = ["All carrots are to be sliced longitudinally,hi",
            "the carrots were repportedly sliced .",
            "The slicing process was well presented."]

filenames = ["doc.txt","report.txt","presentation.txt"]

for content, filename in zip(contents,filenames):
    file = open(f"../files/{filename}",'w')
    file.write(content)
    file.close()