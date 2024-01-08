import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))