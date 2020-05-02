#!/usr/bin/env python
# co

import pandas as pd
df = pd.read_csv(rf"C:\Users\satoryo\Desktop\sample_short.csv", encoding="utf-8")

#行名を参照
df.index

#列名を参照
df.columns

#列名を一括変更。※Listで一括しかできない
df.columns = ['No','Age','Bp','LC','Sex','Wt','Disease']

#列名を指定して変更
df.rename(columns={'No':'ID'})

#行名の一括変更
df.index = ['1','2','3','4','5']

#LC列を削除
df.drop('LC', axis=1)

#3行目を削除
df.drop('3', axis=0)