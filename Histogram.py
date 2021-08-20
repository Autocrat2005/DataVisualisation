#%%
import matplotlib.pyplot as Plt

f = open('agedata.csv', 'r')
agefile = f.readlines()

age_list = []

for records in agefile:
    age_list.append(int(records))

bins = [0, 10 ,20 , 30, 40, 50, 60, 70, 80, 90, 100]

Plt.title("Age Histogram")
Plt.xlabel("Group")
Plt.ylabel("age")

Plt.hist(age_list, bins, histtype='bar', rwidth=0.9)
Plt.show()



# %%
