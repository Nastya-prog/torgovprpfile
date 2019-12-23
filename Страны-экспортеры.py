def Top(x, y):

import pandas as pd
import numpy as np

if y=='2013':
        df1 = pd.read_csv('TCBT_2_I_2013_monthly.csv')
        df1=df1[(df1['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df1['NAPR']==x)]

        df2 = pd.read_csv('TCBT_2_II_2013_monthly.csv')
        df2=df2[(df2['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df2['NAPR']==x)]

        df3 = pd.read_csv('TCBT_2_III_2013_monthly.csv')
        df3=df3[(df3['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df3['NAPR']==x)]

        df4 = pd.read_csv('TCBT_2_IV_2013_monthly.csv')
        df4=df4[(df4['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df4['NAPR']==x)]

    elif y=='2014':
        df1 = pd.read_csv('TCBT_2_I_2014_monthly.csv')
        df1=df1[(df1['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df1['NAPR']==x)]

        df2 = pd.read_csv('TCBT_2_II_2014_monthly.csv')
        df2=df2[(df2['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df2['NAPR']==x)]

        df3 = pd.read_csv('TCBT_2_III_2014_monthly.csv')
        df3=df3[(df3['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df3['NAPR']==x)]

        df4 = pd.read_csv('TCBT_2_IV_2014_monthly.csv')
        df4=df4[(df4['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df4['NAPR']==x)]

    elif y=='2015':
        df1 = pd.read_csv('TCBT_2_I_2015_monthly.csv')
        df1=df1[(df1['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df1['NAPR']==x)]

        df2 = pd.read_csv('TCBT_2_II_2015_monthly.csv')
        df2=df2[(df2['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df2['NAPR']==x)]

        df3 = pd.read_csv('TCBT_2_III_2015_monthly.csv')
        df3=df3[(df3['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df3['NAPR']==x)]

        df4 = pd.read_csv('TCBT_2_IV_2015_monthly.csv')
        df4=df4[(df4['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df4['NAPR']==x)]

    elif y=='2016':
        df1 = pd.read_csv('TCBT_2_I_2016_monthly.csv')
        df1=df1[(df1['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df1['NAPR']==x)]

        df2 = pd.read_csv('TCBT_2_II_2016_monthly.csv')
        df2=df2[(df2['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df2['NAPR']==x)]

        df3 = pd.read_csv('TCBT_2_III_2016_monthly.csv')
        df3=df3[(df3['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df3['NAPR']==x)]

        df4 = pd.read_csv('TCBT_2_IV_2016_monthly.csv')
        df4=df4[(df4['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df4['NAPR']==x)]

    elif y=='2017':
        df1 = pd.read_csv('TCBT_2_I_2017_monthly.csv')
        df1=df1[(df1['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df1['NAPR']==x)]

        df2 = pd.read_csv('TCBT_2_II_2017_monthly.csv')
        df2=df2[(df2['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df2['NAPR']==x)]

        df3 = pd.read_csv('TCBT_2_III_2017_monthly.csv')
        df3=df3[(df3['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df3['NAPR']==x)]


    idf=pd.concat((df1, df2,df3,df4),).reset_index()

    iidf=idf.groupby(["STRANA"])['NETTO'].sum().reset_index()

    iiidf=iidf.sort_values(by ='NETTO', ascending = False)[['STRANA','NETTO']].head(10)

    iiidf.index = pd.Series(iiidf['STRANA'])

    import matplotlib.pyplot as plt
    iiidf.plot.pie(x='STRANA', y='NETTO' ,figsize=(15,15))
    plt.title("Топ 10 стран-экспортеров по НЕТТО за 2013 год")
    plt.show()

    return iiidf

napr=input('Направление (ИМ/ЭК):')
year=input('Год:')
Top(napr, year)