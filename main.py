  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)