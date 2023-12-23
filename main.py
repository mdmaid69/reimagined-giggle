import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()