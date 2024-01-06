def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets