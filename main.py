  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)