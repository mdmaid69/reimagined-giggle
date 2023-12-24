import array
def get_array_buffer_info(array):
        return array.buffer_info()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())