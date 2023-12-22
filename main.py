def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a