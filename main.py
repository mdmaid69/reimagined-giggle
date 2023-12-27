def sort_numbers(numbers):
        return sorted(numbers)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)