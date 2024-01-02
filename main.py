  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)