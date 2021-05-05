import pandas
from scipy import stats

df = pandas.read_csv('experiment.csv', sep=',')

print(df.describe())
print()

print(stats.kstest('norm', 'norm', N=3))
print(stats.kstest('norm', 'norm', N=500))
print(stats.kstest(df, 'norm'))
print()
