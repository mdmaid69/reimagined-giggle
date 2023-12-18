def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue