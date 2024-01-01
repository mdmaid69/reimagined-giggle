sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)