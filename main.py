def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
text = "Hello, world!"
print("Characters:", len(text))