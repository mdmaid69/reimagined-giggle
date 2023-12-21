import array
def get_array_item_count(array, item):
        return array.count(item)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a