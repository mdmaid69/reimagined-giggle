import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)