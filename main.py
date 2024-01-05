import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)