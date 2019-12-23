def Stoim(y):

    import pandas as pd
    import numpy as np

    if y=='2013':
        df1 = pd.read_csv('TCBT_2_I_2013_monthly.csv')
        df1 = df1[(df1['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df1['NAPR']=="ИМ")]

        df2 = pd.read_csv('TCBT_2_II_2013_monthly.csv')
        df2 = df2[(df2['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df2['NAPR']=="ИМ")]

        df3 = pd.read_csv('TCBT_2_III_2013_monthly.csv')
        df3 = df3[(df3['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df3['NAPR']=="ИМ")]

        df4 = pd.read_csv('TCBT_2_IV_2013_monthly.csv')
        df4 = df4[(df4['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df4['NAPR']=="ИМ")]

        df11 = pd.read_csv('TCBT_2_I_2013_monthly.csv')
        df11 = df11[(df11['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df11['NAPR']=="ЭК")]

        df21 = pd.read_csv('TCBT_2_II_2013_monthly.csv')
        df21 = df21[(df21['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df21['NAPR']=="ЭК")]

        df31 = pd.read_csv('TCBT_2_III_2013_monthly.csv')
        df31 = df31[(df31['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df31['NAPR']=="ЭК")]

        df41 = pd.read_csv('TCBT_2_IV_2013_monthly.csv')
        df41 = df41[(df41['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df41['NAPR']=="ЭК")]

    elif y=='2014':
        df1 = pd.read_csv('TCBT_2_I_2014_monthly.csv')
        df1=df1[(df1['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df1['NAPR']=="ИМ")]

        df2 = pd.read_csv('TCBT_2_II_2014_monthly.csv')
        df2=df2[(df2['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df2['NAPR']=="ИМ")]

        df3 = pd.read_csv('TCBT_2_III_2014_monthly.csv')
        df3=df3[(df3['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df3['NAPR']=="ИМ")]

        df4 = pd.read_csv('TCBT_2_IV_2014_monthly.csv')
        df4=df4[(df4['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df4['NAPR']=="ИМ")]

        df11 = pd.read_csv('TCBT_2_I_2014_monthly.csv')
        df11 = df11[(df11['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df11['NAPR']=="ЭК")]

        df21 = pd.read_csv('TCBT_2_II_2014_monthly.csv')
        df21 = df21[(df21['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df21['NAPR']=="ЭК")]

        df31 = pd.read_csv('TCBT_2_III_2014_monthly.csv')
        df31 = df31[(df31['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df31['NAPR']=="ЭК")]

        df41 = pd.read_csv('TCBT_2_IV_2014_monthly.csv')
        df41 = df41[(df41['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df41['NAPR']=="ЭК")]

    elif y=='2015':
        df1 = pd.read_csv('TCBT_2_I_2015_monthly.csv')
        df1=df1[(df1['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df1['NAPR']=="ИМ")]

        df2 = pd.read_csv('TCBT_2_II_2015_monthly.csv')
        df2=df2[(df2['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df2['NAPR']=="ИМ")]

        df3 = pd.read_csv('TCBT_2_III_2015_monthly.csv')
        df3=df3[(df3['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df3['NAPR']=="ИМ")]

        df4 = pd.read_csv('TCBT_2_IV_2015_monthly.csv')
        df4=df4[(df4['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df4['NAPR']=="ИМ")]

        df11 = pd.read_csv('TCBT_2_I_2015_monthly.csv')
        df11 = df11[(df11['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df11['NAPR']=="ЭК")]

        df21 = pd.read_csv('TCBT_2_II_2015_monthly.csv')
        df21 = df21[(df21['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df21['NAPR']=="ЭК")]

        df31 = pd.read_csv('TCBT_2_III_2015_monthly.csv')
        df31 = df31[(df31['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df31['NAPR']=="ЭК")]

        df41 = pd.read_csv('TCBT_2_IV_2015_monthly.csv')
        df41 = df41[(df41['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df41['NAPR']=="ЭК")]

    elif y=='2016':
        df1 = pd.read_csv('TCBT_2_I_2016_monthly.csv')
        df1=df1[(df1['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df1['NAPR']=="ИМ")]

        df2 = pd.read_csv('TCBT_2_II_2016_monthly.csv')
        df2=df2[(df2['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df2['NAPR']=="ИМ")]

        df3 = pd.read_csv('TCBT_2_III_2016_monthly.csv')
        df3=df3[(df3['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df3['NAPR']=="ИМ")]

        df4 = pd.read_csv('TCBT_2_IV_2016_monthly.csv')
        df4=df4[(df4['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df4['NAPR']=="ИМ")]

        df11 = pd.read_csv('TCBT_2_I_2016_monthly.csv')
        df11 = df11[(df11['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df11['NAPR']=="ЭК")]

        df21 = pd.read_csv('TCBT_2_II_2016_monthly.csv')
        df21 = df21[(df21['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df21['NAPR']=="ЭК")]

        df31 = pd.read_csv('TCBT_2_III_2016_monthly.csv')
        df31 = df31[(df31['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df31['NAPR']=="ЭК")]

        df41 = pd.read_csv('TCBT_2_IV_2016_monthly.csv')
        df41 = df41[(df41['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df41['NAPR']=="ЭК")]

    elif y=='2017':
        df1 = pd.read_csv('TCBT_2_I_2017_monthly.csv')
        df1=df1[(df1['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df1['NAPR']=="ИМ")]

        df2 = pd.read_csv('TCBT_2_II_2017_monthly.csv')
        df2=df2[(df2['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df2['NAPR']=="ИМ")]

        df3 = pd.read_csv('TCBT_2_III_2017_monthly.csv')
        df3=df3[(df3['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df3['NAPR']=="ИМ")]

        df11 = pd.read_csv('TCBT_2_I_2017_monthly.csv')
        df11 = df11[(df11['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df11['NAPR']=="ЭК")]

        df21 = pd.read_csv('TCBT_2_II_2017_monthly.csv')
        df21 = df21[(df21['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df21['NAPR']=="ЭК")]

        df31 = pd.read_csv('TCBT_2_III_2017_monthly.csv')
        df31 = df31[(df31['REGION']=="78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ")&(df31['NAPR']=="ЭК")]


    idf=pd.concat((idf1, idf2,idf3,idf4),).reset_index()

    if x==2017:
        idfnew=pd.concat((idf11, idf22,idf33),).reset_index()
    else:
        idfnew=pd.concat((idf11, idf22,idf33,idf44),).reset_index()

    idf.index = pd.Series(idf['PERIOD'])
    idfnew.index = pd.Series(idfnew['PERIOD'])

    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(7,7))

    plt.plot(idf['STOIM'], label="Импорт")
    plt.plot(idfnew['STOIM'], label="Экспорт")

    plt.xticks(rotation=70)
    plt.legend()
    plt.title("Общая стоимость по месяцам за год")

    plt.show()

    return(idf, idfnew)

year=input('Год:')
Stoim(year)