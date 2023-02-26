
import pandas as  pd
file_path= input("file_path")
file=pd.read_csv(file_path)
df=pd.DataFrame(file)
print( df)

import matplotlib.pyplot as plt


labels = df["month"]
fridge = df["fridge"]
tv = df["tv"]
washmac = df["washing"]


fig, ax = plt.subplots()


ax.bar(labels, fridge, label='FRIDGE')
ax.bar(labels, tv, bottom=fridge, label='TV')
ax.bar(labels, washmac, bottom=[i+j for i,j in zip(fridge,tv)], label='WASHING MACHINE')

ax.set_xlabel('month')
ax.set_ylabel('sales')
ax.set_title('Stacked sales bar')
ax.legend()


plt.show()