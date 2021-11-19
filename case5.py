import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('countries of the world.csv')

df.fillna(-1, inplace=True)

x = df['Status Rocket']
z = df['Status Mission']
c = df[df['Status Mission'] == 'Status Rocket'].values_count()
print(f'Количество Миссий где статус миссии и ракеты равны {c}')
s = pd.Series(data=x, index=z)
s.plot()
plt.show()
