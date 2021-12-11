import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance .csv')

df.fillna(-1, inplace=True)

x = df[df['parental level of education' == 'high school']]
x = x[x['math score'] >= 85].values_count()

print(x / len(df.index)*100)

s = pd.Series(data=df['parental level of education'], index=df['math score'])
s.plot()
plt.show()
