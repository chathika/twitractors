import pandas as pd
import matplotlib.pyplot as plt
import sys
headers = ['time', 'polarity', 'subjectivity']
dtypes = {'time': 'str', 'polarity': 'float', 'subjectivity': 'float'}
parse_dates = ['time']
all_data = pd.read_csv(sys.argv[1], skiprows=[1],names=headers, dtype=dtypes, parse_dates=parse_dates)
print(all_data.head(5))

all_data.head(10000).plot(style=".")#.scatter(x='time',y='polarity')
plt.show()
all_data.plot(style=".")#.scatter(x='time',y='polarity')
plt.show()
#all_data.plot#.scatter(x='time',y='subjectivity')
#plt.show()