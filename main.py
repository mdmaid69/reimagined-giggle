sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
def is_palindrome(s):
        return s == s[::-1]