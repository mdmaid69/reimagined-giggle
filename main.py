  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import random
def roll_die():
        return random.randint(1, 6)