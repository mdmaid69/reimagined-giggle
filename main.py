text = "Hello, world!"
print("Uppercase:", text.upper())
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)