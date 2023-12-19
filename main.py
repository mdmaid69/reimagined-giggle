def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())