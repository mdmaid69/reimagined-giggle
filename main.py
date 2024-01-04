  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a