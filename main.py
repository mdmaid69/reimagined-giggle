def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time