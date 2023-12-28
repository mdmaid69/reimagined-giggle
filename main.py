import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"