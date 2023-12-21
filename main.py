def calculate_average(lst):
        return sum(lst) / len(lst)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())