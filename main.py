import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"