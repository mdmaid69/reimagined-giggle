def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())