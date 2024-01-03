def find_unique_words(sentence):
        return set(sentence.split())
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)