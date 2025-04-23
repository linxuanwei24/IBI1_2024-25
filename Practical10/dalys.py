import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv") # The code for importing the .csv file works
print(dalys_data.head(10))
print(dalys_data.describe())
# The maximal DALYs is 693367.490000. The minimum is 15045.110000. The first year when DALYs were recorded is 1990. The most recent year is 2019.
print(dalys_data.iloc[0:10 , 2]) # There is correct code for showing the third column (the year) for the first 10 rows (inclusive).
# The 10th year in Afganistan is 1999.
print(dalys_data.loc[dalys_data["Year"] == 1990 ,"DALYs"]) # show DALYs for all countries in 1990

uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data.Entity == "France" , ["DALYs", "Year"]]
print(uk["DALYs"].describe().loc["mean"])       # The mean of DALYs of the UK is 23319.016333333333
print(france["DALYs"].describe().loc["mean"])   # The mean of DALYs of the UK is 21474.627000000004
# The mean DALYs in the UK was greater than France.

plt.plot(uk.Year, uk.DALYs, 'bo')
plt.xticks(uk.Year,rotation=-90)
plt.title("The DALYs in The UK")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.show()

print(dalys_data.loc[dalys_data["DALYs"] > 650000 , "Entity"]) # Rwanda has recorded a DALYs greater than 650,000 in a single year.