import pandas as pd
import numpy as np
import random

date_rng  = pd.date_range('2018-01-01', '2019-12-31',freq='1H')
temp = np.random.randint(-30.0, 40.0,(17497,))
df = pd.DataFrame({'CO2':temp},index=pd.to_datetime(date_rng))
df.insert(1, 'year', df.index.year)
df.insert(2, 'month', df.index.month)
df.insert(3, 'day', df.index.day)
df.insert(4, 'hour', df.index.hour)
df = df.copy()
yyyy = df['year'].unique()
month = df['month'].unique()

import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(figsize=(10,5), nrows=2, ncols=12)

for m, ax in zip(range(1,25), axes.flat):
    if m <= 12:
        y = yyyy[0]
        df1 = df[(df['year'] == y) & (df['month'] == m)]
    else:
        y = yyyy[1]
        m -= 12
        df1 = df[(df['year'] == y) & (df['month'] == m)]
    df1 = df1.pivot_table(index="hour",columns="day",values='CO2',aggfunc="mean")
    plt.figure(m)
    sns.heatmap(df1, cmap='RdBu', cbar=False, ax=ax)

plt.show()