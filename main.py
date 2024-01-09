text = "Hello, world!"
print("Words:", len(text.split()))
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)