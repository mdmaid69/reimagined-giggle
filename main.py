import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"