import datetime
def get_current_datetime():
        return datetime.datetime.now()
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a