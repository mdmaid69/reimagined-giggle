import array
def get_bytes_from_array(array):
        return array.tobytes()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())