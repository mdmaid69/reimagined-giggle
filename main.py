  def is_even(n):
        return n % 2 == 0
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)