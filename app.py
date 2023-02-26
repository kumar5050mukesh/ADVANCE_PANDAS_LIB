import matplotlib.pyplot as plt

categories = ['jan', 'feb', 'mar', 'apr', 'may']
sales_of_tv = [20, 35, 30, 25, 10]
sales_of_fridge = [10, 20, 25, 30, 35]
sales_of_washing = [15, 15, 15, 15, 15]

import matplotlib.pyplot as plt


labels = ['jan', 'feb', 'mar', 'apr', 'may']
fridge = [20, 35, 30, 25, 15]
tv = [10, 20, 25, 15, 30]
washmac = [5, 10, 15, 20, 25]


fig, ax = plt.subplots()


ax.bar(labels, fridge, label='FRIDGE')
ax.bar(labels, tv, bottom=fridge, label='TV')
ax.bar(labels, washmac, bottom=[i+j for i,j in zip(fridge,tv)], label='WASHING MACHINE')

ax.set_xlabel('month')
ax.set_ylabel('sales')
ax.set_title('Stacked sales bar')
ax.legend()


plt.show()
