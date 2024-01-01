def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])