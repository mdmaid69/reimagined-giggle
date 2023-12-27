import glob
def find_files(pattern):
        return glob.glob(pattern)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"