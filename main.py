def count_words(sentence):
        return len(sentence.split())
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)