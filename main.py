import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)