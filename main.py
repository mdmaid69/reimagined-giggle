import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import logging
def setup_logging(level):
        logging.basicConfig(level=level)