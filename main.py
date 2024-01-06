def count_characters(sentence):
        return len(sentence)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)