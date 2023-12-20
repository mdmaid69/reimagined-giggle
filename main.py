import array
def convert_array_to_bytes(array):
        return array.tobytes()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())