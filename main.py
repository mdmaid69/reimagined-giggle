def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def find_unique_words(sentence):
        return set(sentence.split())