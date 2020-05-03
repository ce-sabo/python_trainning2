#必要なライブラリのimport
import pickle
import pandas as pd
import datetime

#CSVファイルを読み込みDataFrameにする
df = pd.read_csv(rf"C:\Users\satoryo\Desktop\date_2020.csv", encoding="utf-8")

#DateFrameのobjectの列からdatetime型の列を作成して追加する
df["datetime"] = pd.to_datetime(df["date"])

#dateの列から年:Year、月:Month、日:Dayそれぞれの列を作成
df["Year"] = df["datetime"].dt.year
df["Month"] = df["datetime"].dt.month
df["Day"] = df["datetime"].dt.day

#object列、date列を削除
df.drop(["date", "datetime"], axis=1)