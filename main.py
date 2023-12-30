def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))