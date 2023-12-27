def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)