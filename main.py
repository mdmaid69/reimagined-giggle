import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)