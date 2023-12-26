def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_volume(length, width, height):
        return length * width * height