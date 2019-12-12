import pandas as pd
import numpy as np

df1 = pd.read_csv('TCBT_2_I_2013_monthly.csv')
df1=df1[(df1['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df1['NAPR']=="ИМ")]
idf1=df1.groupby(['PERIOD','NAPR'])['STOIM'].sum()

df2 = pd.read_csv('TCBT_2_II_2013_monthly.csv')
df2=df2[(df2['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df2['NAPR']=="ИМ")]
idf2=df2.groupby(['PERIOD', 'NAPR'])['STOIM'].sum()

df3 = pd.read_csv('TCBT_2_III_2013_monthly.csv')
df3=df3[(df3['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df3['NAPR']=="ИМ")]
idf3=df3.groupby(['PERIOD', 'NAPR'])['STOIM'].sum()

df4 = pd.read_csv('TCBT_2_IV_2013_monthly.csv')
df4=df4[(df4['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df4['NAPR']=="ИМ")]
idf4=df4.groupby(['PERIOD', 'NAPR'])['STOIM'].sum()

idf=pd.concat((idf1, idf2,idf3,idf4),).reset_index()


print(idf)

#######################

df11 = pd.read_csv('TCBT_2_I_2013_monthly.csv')
df11=df11[(df11['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df11['NAPR']=="ЭК")]
idf11=df11.groupby(['PERIOD','NAPR'])['STOIM'].sum()

df22 = pd.read_csv('TCBT_2_II_2013_monthly.csv')
df22=df22[(df22['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df22['NAPR']=="ЭК")]
idf22=df22.groupby(['PERIOD', 'NAPR'])['STOIM'].sum()

df33 = pd.read_csv('TCBT_2_III_2013_monthly.csv')
df33=df33[(df33['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df33['NAPR']=="ЭК")]
idf33=df33.groupby(['PERIOD', 'NAPR'])['STOIM'].sum()

df44 = pd.read_csv('TCBT_2_IV_2013_monthly.csv')
df44=df44[(df44['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df44['NAPR']=="ЭК")]
idf44=df44.groupby(['PERIOD', 'NAPR'])['STOIM'].sum()

idfnew=pd.concat((idf11, idf22,idf33,idf44),).reset_index()
print(idfnew)
###################

idf.index = pd.Series(idf['PERIOD'])
idfnew.index = pd.Series(idfnew['PERIOD'])

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(7,7))

plt.plot(idf['STOIM'], label="Импорт")
plt.plot(idfnew['STOIM'], label="Экспорт")

plt.xticks(rotation=70)
plt.legend()
plt.title("Общая стоимость по месяцам за 2013 год")


plt.show()


