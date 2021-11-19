import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('countries of the world.csv')

df.fillna(-1, inplace=True)

x = df['Total Fat']
z = df['Total Fat (% Daily Value)']

print(f'Общего жира в одном проценте {x/z}')
s = pd.Series(data=x, index=z)
s.plot()
plt.show()
