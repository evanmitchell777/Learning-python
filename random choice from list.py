#this program prints random stiuff from each of the lists add whatever 
from random import choice
list1 =["stuff"]
list2 = ["stuff"]
list3 = ["stuff"]

phrase = "here you can print three random things {0} from {1} the list! {2}".format(choice(list1),choice(list2),choice(list3))

print(phrase)
