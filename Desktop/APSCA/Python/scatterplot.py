import matplotlib.pyplot as plt
import numpy as np


class scatter:
    def run(x,y,lowerlimx,lowerlimy, upperlimx, upperlimy, sizes = [], colors = [], vmin = 0, vmax = 0):
        plt.style.use('_mpl-gallery')
        fig, ax = plt.subplots()
        if(len(sizes) != 0 and len(colors) != 0):
            ax.scatter(x, y, s=sizes, c=colors, vmin=vmin, vmax=vmax)
        elif(len(sizes) != 0):
            ax.scatter(x, y, s=sizes, vmin=vmin, vmax=vmax)
        else:
            ax.scatter(x, y, s = 20, vmin=vmin, vmax=vmax)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

        ax.set(xlim=(lowerlimx, upperlimx), xticks=np.arange(lowerlimx+1, upperlimx),
            ylim=(lowerlimy, upperlimy), yticks=np.arange(lowerlimy+1, upperlimy))
    


    plt.show()



# make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))
scatter(x,y,0,0,10,10,sizes,colors,0,40)

