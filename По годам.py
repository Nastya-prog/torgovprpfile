import pandas as pd
import numpy as np


def Year(x, z):
#2013
    df13 = pd.read_csv('TCBT_2_I_2013_monthly.csv')
    df13=df13[(df13['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df13['NAPR']==x)&(df13['TNVED']==z)]

    df23 = pd.read_csv('TCBT_2_II_2013_monthly.csv')
    df23=df23[(df23['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df23['NAPR']==x)&(df23['TNVED']==z)]

    df33 = pd.read_csv('TCBT_2_III_2013_monthly.csv')
    df33=df33[(df33['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df33['NAPR']==x)&(df33['TNVED']==z)]

    df43 = pd.read_csv('TCBT_2_IV_2013_monthly.csv')
    df43=df43[(df43['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df43['NAPR']==x)&(df43['TNVED']==z)]

#2014
    df14 = pd.read_csv('TCBT_2_I_2014_monthly.csv')
    df14=df14[(df14['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df14['NAPR']==x)&(df14['TNVED']==z)]

    df24 = pd.read_csv('TCBT_2_II_2014_monthly.csv')
    df24=df24[(df24['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df24['NAPR']==x)&(df24['TNVED']==z)]

    df34 = pd.read_csv('TCBT_2_III_2014_monthly.csv')
    df34=df34[(df34['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df34['NAPR']==x)&(df34['TNVED']==z)]

    df44 = pd.read_csv('TCBT_2_IV_2014_monthly.csv')
    df44=df44[(df44['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df44['NAPR']==x)&(df44['TNVED']==z)]

#2015
    df15 = pd.read_csv('TCBT_2_I_2015_monthly.csv')
    df15=df15[(df15['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df15['NAPR']==x)&(df15['TNVED']==z)]

    df25 = pd.read_csv('TCBT_2_II_2015_monthly.csv')
    df25=df25[(df25['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df25['NAPR']==x)&(df25['TNVED']==z)]

    df35 = pd.read_csv('TCBT_2_III_2015_monthly.csv')
    df35=df35[(df35['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df35['NAPR']==x)&(df35['TNVED']==z)]

    df45 = pd.read_csv('TCBT_2_IV_2015_monthly.csv')
    df45=df45[(df45['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df45['NAPR']==x)&(df45['TNVED']==z)]

#2016
    df16 = pd.read_csv('TCBT_2_I_2016_monthly.csv')
    df16=df16[(df16['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df16['NAPR']==x)&(df16['TNVED']==z)]

    df26 = pd.read_csv('TCBT_2_II_2016_monthly.csv')
    df26=df26[(df26['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df26['NAPR']==x)&(df26['TNVED']==z)]

    df36 = pd.read_csv('TCBT_2_III_2016_monthly.csv')
    df36=df36[(df36['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df36['NAPR']==x)&(df36['TNVED']==z)]

    df46 = pd.read_csv('TCBT_2_IV_2016_monthly.csv')
    df46=df46[(df46['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df46['NAPR']==x)&(df46['TNVED']==z)]

#2017
    df17 = pd.read_csv('TCBT_2_I_2017_monthly.csv')
    df17=df17[(df17['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df17['NAPR']==x)&(df17['TNVED']==z)]

    df27 = pd.read_csv('TCBT_2_II_2017_monthly.csv')
    df27=df27[(df27['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df27['NAPR']==x)&(df27['TNVED']==z)]

    df37 = pd.read_csv('TCBT_2_III_2017_monthly.csv')
    df37=df37[(df37['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df37['NAPR']==x)&(df37['TNVED']==z)]

    idf13=pd.concat((df13, df23,df33,df43),).reset_index()
    idf14=pd.concat((df14, df24,df34,df44),).reset_index()
    idf15=pd.concat((df15, df25,df35,df45),).reset_index()
    idf16=pd.concat((df16, df26,df36,df46),).reset_index()
    idf17=pd.concat((df17, df27,df37),).reset_index()

    iidf13=idf13.groupby(["NAPR"])['STOIM'].sum().reset_index()
    iidf14=idf14.groupby(["NAPR"])['STOIM'].sum().reset_index()
    iidf15=idf15.groupby(["NAPR"])['STOIM'].sum().reset_index()
    iidf16=idf16.groupby(["NAPR"])['STOIM'].sum().reset_index()
    iidf17=idf17.groupby(["NAPR"])['STOIM'].sum().reset_index()

    idff=pd.concat((iidf13, iidf14,iidf15,iidf16,iidf17),).reset_index()

    import matplotlib.pyplot as plt
    idff.plot.bar(x="index", y='STOIM' ,figsize=(10,10))
    plt.title("Стоимость продукта в разрезе годов")
    plt.show()

    return idff


napr=input('Направление (ЭК/ИМ):')
tnved=input('Код товара:')
Year(napr, tnved)





