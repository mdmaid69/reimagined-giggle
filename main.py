def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a