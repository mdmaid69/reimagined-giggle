def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
def find_unique_words(sentence):
        return set(sentence.split())