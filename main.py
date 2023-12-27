import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"