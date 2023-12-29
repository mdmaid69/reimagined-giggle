def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
i = 0
while i < 5:
        print(i)
        i += 1