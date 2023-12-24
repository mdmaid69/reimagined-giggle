def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())