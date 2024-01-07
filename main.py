  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import shutil
def delete_directory(path):
        shutil.rmtree(path)