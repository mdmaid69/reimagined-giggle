def count_words(sentence):
        return len(sentence.split())
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)