import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)