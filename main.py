def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))