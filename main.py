import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"