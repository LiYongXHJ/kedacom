# coding=utf-8

import pandas as pd
import numpy as np
import datetime

df = pd.DataFrame(np.random.randn(8, 3), index=pd.date_range('20181112', periods=8), columns=list('ABC'))
# wp = pd.Panel(np.random.randn(2, 5, 4), items=['item1', 'item2'], major_axis=pd.date_range('20181112', periods=5),
#               minor_axis=list('ABCD'))

# df.columns = [x.lower() for x in df.columns]
#
# df = pd.DataFrame({"one": pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
#                    "two": pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
#                    "three": pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})
#
# print(df)
# row = df.iloc[1]
# column = df['two']
#
# print(df.sub(row, axis=1))

# print(df)
print(type(df.describe()))