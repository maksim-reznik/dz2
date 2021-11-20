import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('countries of the world.csv')

df.fillna(-1, inplace=True)

x = df['Infant mortality (per 1000 births)']
z = df['Deathrate']
x1 = x.values_counts()
z1 = z.values_counts()
print(f'Смертоность детей меньше чем смертность людей на {z1 - x1}')
s = x
s.plot(kind= 'hist')
s1 = z
s1.plot(kind='hist')
plt.show()


# на сколько  смертность детей меньше взрослых
