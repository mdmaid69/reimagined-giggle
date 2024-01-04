def is_palindrome(s):
        return s == s[::-1]
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))