import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import sys
  def get_python_version():
        return sys.version