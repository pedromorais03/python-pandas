import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, np.nan, 5, 6])
type(s)

dates = pd.date_range('20180101', periods= 6, freq="M")
print(dates)