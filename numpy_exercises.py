import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?
print(a)
np.count_nonzero(a < 0)

# 2. How many positive numbers are there?
print (a)
np.count_nonzero(a > 0)

# 3. How many even positive numbers are there?
is_pos = a > 0
is_even = a % 2 == 0
pos_even = is_pos & is_even
a[pos_even].size

# 3. option a
a[(a > 0) & (a % 2 == 0)].size 

# 3. option b
((a > 0) & (a % 2 == 0)).sum()

# 4. If you were to add 3 to each data point, how many positive numbers would there be?
posnum = a + 3
print (posnum)
np.count_nonzero(posnum > 0)

# 5. If you squared each number, what would the new mean and standard deviation be?
squared = np.square(a)
print(squared)
new_mean = squared.mean()
print(new_mean)
new_std = squared.std()
print(new_std)

# 6. A common statistical operation on a dataset is centering. 
#    This means to adjust the data such that the mean of the data is 0. 
#    This is done by subtracting the mean from each data point. 
#    Center the data set. See this link for more on centering.
avg = a.mean()
avg
a - avg
(a - a.mean()).mean()

# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# z = (x-μ)/σ, x is the raw score, μ is the population mean, σ is the population standard deviation
from scipy import stats
stats.zscore(a)

