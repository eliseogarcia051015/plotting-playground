#import library as nickname/allias 
import matplotlib.pyplot as plt


# Create a figure (a window for the plot) with:
fig = plt.figure(figsize=(5,5), facecolor='white',layout='constrained')
 #title
fig.suptitle("Practice 1")
#Add a single subplot (axes) to the figure
ax = fig.add_subplot()
#bx = fig.add_subplot()
# Set a title for the axes (the individual plot area)
ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')
#bx.set_title('HELLO', loc='right', fontstyle='oblique', fontsize='medium')

#display everything
plt.show()