import numpy as np

# create a 3 x 5 matrix of numbers in range 0-14
a = np.arange(15).reshape(3, 5)

print a
print a.shape
print a.ndim

import pandas as pd

s = pd.Series([1,3,5,np.nan,6,8])

print s