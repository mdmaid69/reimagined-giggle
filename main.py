n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list