import shutil
def delete_directory(path):
        shutil.rmtree(path)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"