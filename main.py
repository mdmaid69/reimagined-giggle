import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])