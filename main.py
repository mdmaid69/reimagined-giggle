  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)