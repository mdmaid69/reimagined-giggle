  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()