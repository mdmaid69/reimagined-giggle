numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)