def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities