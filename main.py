def reverse_string(s):
        return s[::-1]
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)