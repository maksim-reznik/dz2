import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IMDB-Movie-Data.csv')

df.fillna(-1, inplace=True)


s = pd.Series(data=df['year'], index=df['Runtime (Minutes)'])
s.plot()
plt.show()
