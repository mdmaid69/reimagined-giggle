import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)