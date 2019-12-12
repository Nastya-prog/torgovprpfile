import pandas as pd
import numpy as np

df1 = pd.read_csv('TCBT_2_I_2013_monthly.csv')
df1=df1[(df1['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df1['NAPR']=="ЭК")]

df2 = pd.read_csv('TCBT_2_II_2013_monthly.csv')
df2=df2[(df2['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df2['NAPR']=="ЭК")]

df3 = pd.read_csv('TCBT_2_III_2013_monthly.csv')
df3=df3[(df3['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df3['NAPR']=="ЭК")]

df4 = pd.read_csv('TCBT_2_IV_2013_monthly.csv')
df4=df4[(df4['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df4['NAPR']=="ЭК")]

idf=pd.concat((df1, df2,df3,df4),).reset_index()

iidf=idf.groupby(["STRANA"])['NETTO'].sum().reset_index()

iiidf=iidf.sort_values(by ='NETTO', ascending = False)[['STRANA','NETTO']].head(10)

iiidf.index = pd.Series(iiidf['STRANA'])
print(iiidf)

import matplotlib.pyplot as plt
iiidf.plot.pie(x='STRANA', y='NETTO' ,figsize=(15,15))
plt.title("Топ 10 стран-экспортеров по НЕТТО за 2013 год")
plt.show()

