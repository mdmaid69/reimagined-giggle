def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
def sort_numbers(numbers):
        return sorted(numbers)