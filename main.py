def greet(name):
        print(f"Hello, {name}!")
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)