def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)