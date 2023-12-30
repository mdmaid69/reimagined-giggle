  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import random
def roll_die():
        return random.randint(1, 6)