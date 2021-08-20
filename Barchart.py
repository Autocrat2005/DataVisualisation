#%%
import matplotlib.pyplot as Plt

x_cities = ['New York', 'London', 'Dubai', 'New Delhi', 'Tokyo']
y_temp = [75, 65, 105, 98, 90]

Plt.title("Tempraure Variations")
Plt.xlabel("Cities")
Plt.ylabel("Temprature")

Plt.bar(x_cities, y_temp)
Plt.show()

# %%
