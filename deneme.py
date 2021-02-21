import pandas as pd
import numpy as np
from pandas import DataFrame, Series
df = pd.DataFrame(data = np.arange(6).reshape(2,3), index=["index1","index2"],
                columns=["col1","col2","col3"])
print(df)