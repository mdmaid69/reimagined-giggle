def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_average(lst):
        return sum(lst) / len(lst)