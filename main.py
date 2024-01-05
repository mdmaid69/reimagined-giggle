def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_roi(gain, cost):
        return (gain - cost) / cost