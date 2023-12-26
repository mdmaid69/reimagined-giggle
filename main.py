  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"