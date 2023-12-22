  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a