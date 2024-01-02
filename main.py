  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)