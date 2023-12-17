def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)