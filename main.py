import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))