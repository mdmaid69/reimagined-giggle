sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)