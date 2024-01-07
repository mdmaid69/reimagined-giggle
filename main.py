  import sys
  def get_python_version():
        return sys.version
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()