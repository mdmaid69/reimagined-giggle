import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])