  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a