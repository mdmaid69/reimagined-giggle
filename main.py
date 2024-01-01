numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)