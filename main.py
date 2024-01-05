  import sys
  def get_python_version():
        return sys.version
import shutil
def move_file(src, dst):
        shutil.move(src, dst)