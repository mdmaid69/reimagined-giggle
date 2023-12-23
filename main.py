def remove_duplicates(lst):
        return list(set(lst))
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])