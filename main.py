import shutil
def delete_directory(path):
        shutil.rmtree(path)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"