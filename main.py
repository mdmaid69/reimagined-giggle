def find_union(list1, list2):
        return set(list1) | set(list2)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])