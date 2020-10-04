count= 0
text = open("rome.txt", "r")
l = list()
for line in text:
    words = line.split(" ")
for i in range(len(words)):
    if str(words[i]) == "rome":
        count+=1 
    else: 
        pass 
print (count)