import matplotlib.pyplot as plt
import numpy as np

def easybar(x,y,lowerx,lowery,upperlimx, upperlimy, wd = 1, lw = 0.7):
    plt.style.use('_mpl-gallery')

    # plot
    fig, ax = plt.subplots()

    ax.bar(x, y, width=wd, edgecolor="black", linewidth=lw)

    ax.set(xlim=(lowerx, upperlimx), xticks=np.arange(lowerx+1, upperlimx),
        ylim=(lowery, upperlimy), yticks=np.arange(lowery+1, upperlimy))

    plt.show()

# make data:
x = 0.5 + np.arange(8)
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]
easybar(x,y,0,0,8,8)
