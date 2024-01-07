import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)