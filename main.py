def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))