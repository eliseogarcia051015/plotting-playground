import numpy as np
import matplotlib.pyplot as plt

categories = np.array(["Freshmen", "Sophomores", "Juniors", "Seniors"])
values = np.array([300, 250, 275, 225])
colors = np.array(["red", "yellow", "blue", "green"])

plt.pie(values, labels=categories, 
                autopct="%1.1f%%", 
                colors=colors,
                explode=[0,0,0,0.1],
                shadow=True,
                startangle=90)
plt.title("School Student Distribution")
plt.show()