#%%
import matplotlib.pyplot as Plt

f = open('agedata2.csv', 'r')
agefile = f.readlines()

city_list = []

for records in agefile:
    age , city = records.split(sep= ',')
    city_list.append(city)

from collections import Counter
city_count = Counter(city_list)

city_names = list(city_count.keys())
city_values = list(city_count.values())

Plt.pie(city_values, labels=city_names, autopct='%.2f%%')
Plt.show()




# %%
