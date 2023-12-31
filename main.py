import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  def is_odd(n):
        return n % 2 != 0