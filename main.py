def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())