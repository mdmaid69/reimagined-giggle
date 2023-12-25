def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))