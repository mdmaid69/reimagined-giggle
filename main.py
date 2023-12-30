  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)