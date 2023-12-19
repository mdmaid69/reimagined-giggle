import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()