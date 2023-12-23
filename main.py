import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))