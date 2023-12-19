def calculate_average(numbers):
        return sum(numbers) / len(numbers)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)