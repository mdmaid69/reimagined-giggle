sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)