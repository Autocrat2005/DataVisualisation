import matplotlib.pyplot as Plt

f = open('agedata2.csv', 'r')
salefile = f.readlines()

s_list = []
c_list = []

for records in salefile:
    sale, cost = records.split(sep=',')
    s_list.append(int(sale))
    c_list.append(int(cost))

    Plt.title("Sales vs Cost")
    Plt.xlabel("Sale")
    Plt.ylabel("cost")

    Plt.scatter(s_list, c_list)
    Plt.show()

