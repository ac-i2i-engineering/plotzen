import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')


class line:
    def twolineplot(x, y, x2, y2,Xlower,Ylower,Xupper,Yupper,width = 1):
        fig, ax = plt.subplots()

        ax.plot(x, y, "o-", linewidth=width)
        ax.plot(x2, y2, 'x-', linewidth=width)

        ax.set(xlim=(Xlower, Xupper), xticks=np.arange(Xlower + 1, Xupper),
            ylim=(Ylower, Yupper), yticks=np.arange(Ylower + 1, Yupper))

        plt.show()

def run(x, y,Xlower,Ylower,Xupper,Yupper,width = 1):
        fig, ax = plt.subplots()
        if x.ndim == 1:
            ax.plot(x, y, "o-", linewidth=width)
        else:
            for i in range(len(x)):
                ax.plot(x[i], y[i], "o-", linewidth=width)

        ax.set(xlim=(Xlower, Xupper), xticks=np.arange(Xlower + 1, Xupper),
            ylim=(Ylower, Yupper), yticks=np.arange(Ylower + 1, Yupper))

        plt.show()

x = np.linspace(0, 10, 25)
y = 4 + 1 * np.sin(2 * x)
x2 = np.linspace(0, 20, 25)
y2 = 4 + 1 * np.sin(1 * x2)
xc = np.array([x,x2])
yc = np.array([y,y2])
run(xc, yc,0,0,10,10)