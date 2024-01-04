def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_perpetuity(payment, rate):
        return payment / rate