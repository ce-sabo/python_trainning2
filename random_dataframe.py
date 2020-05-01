import pandas as pd
import numpy as np

#100個の整数(int)をrandomに生成
a = np.random.randint(0, 100, 100)

#100個の一様乱数(0~1)をrandomに生成
b = np.random.rand(100)

#100個の正規乱数(任意の平均,標準偏差)に従う乱数を生成
c = np.random.normal(1, 1, 100)

#作成したarryをDataFrameに格納する、列名も変える
df = pd.DataFrame({'A':a, 'B':b, 'C':c })
