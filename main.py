def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))