import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())