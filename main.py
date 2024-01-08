text = "Hello, world!"
print("Reversed:", text[::-1])
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)