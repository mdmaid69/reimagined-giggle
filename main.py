import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)