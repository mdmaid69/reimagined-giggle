def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities