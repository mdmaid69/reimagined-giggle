  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)