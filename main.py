import re
print(re.match("h.*o", "hello world"))
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)