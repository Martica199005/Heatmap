import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

#%matplotlib inline
#%matplotlib notebook

df=pd.read_excel("finished.xls")
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month

df2=df[["H","T","HI","year","month"]]
#years= 2015,2016,2017,2018,2019
list_year=df2["year"].unique()

for y in list_year:
  df3=df2.groupby(df2['year']).filter(lambda x: ((x.year ==y)).all())
  #months for each year
  list_month=df3["month"].unique()
  for m in list_month:
    mydate = datetime.datetime.strptime(str(m), '%m')

    df4=df3.groupby(df2['month']).filter(lambda x: ((x.month ==m)).all())
    plt.figure(figsize=(10,5))
    # create pivot table, H will be columns, T will be rows
    piv = pd.pivot_table(df4, values="HI",index=["H"], columns=["T"], fill_value=0)
    #plot pivot table as heatmap using seaborn
    ax = sns.heatmap(piv)
    title="Correlation "+"year "+str(y)+" in "+str(mydate.strftime('%B'))
    plt.title(title, fontsize=30)
    plt.setp( ax.xaxis.get_majorticklabels(), rotation=90 )
    plt.tight_layout()
    plt.show()



