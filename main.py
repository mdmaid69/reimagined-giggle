import glob
def find_files(pattern):
        return glob.glob(pattern)
  def remove_duplicates(lst):
        return list(set(lst))