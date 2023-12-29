import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))