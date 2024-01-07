text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
def find_difference(list1, list2):
        return set(list1) - set(list2)