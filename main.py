import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))