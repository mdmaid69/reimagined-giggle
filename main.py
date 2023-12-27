  def is_even(n):
        return n % 2 == 0
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)