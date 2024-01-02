def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)