  import os
  def delete_file(file_name):
        os.remove(file_name)
import random
def roll_die():
        return random.randint(1, 6)