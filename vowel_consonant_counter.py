vowels = ['a','e','i','o','u']
sentence = input("enter sentence: ")
sentence = sentence.lower()
sentence:list = sentence
vowel_count=0
consoant_counter=0
for letter in sentence:
    if letter in vowels:
        vowel_count+=1
    elif letter not in vowels:
        consoant_counter+=1
    else:
        pass

print("There are "+str(vowel_count)+" Vowels and there are "+str(consoant_counter),"Consonants")
