import glob
def find_files(pattern):
        return glob.glob(pattern)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"