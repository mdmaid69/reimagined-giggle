  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)