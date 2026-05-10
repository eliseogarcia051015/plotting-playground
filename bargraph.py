#learn other types of visulizations in matplotlib
import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruit", "Vegetables", "Proteins", "Dairy", "Sweets"])
values = np.array([4,3,2,5,3,1])

#plt.bar(categories, values, color="skyblue")
plt.barh(categories, values, color="skyblue")

plt.title('Daily Consumption')
plt.xlabel("Food")
plt.ylabel("Quantity")
plt.show()