  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list