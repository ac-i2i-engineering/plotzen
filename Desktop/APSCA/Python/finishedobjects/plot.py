import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

class scatter():
    
    def __init__(self,type,x,y,lowerlimx = None,lowerlimy = None, upperlimx = None, upperlimy = None, sizes = [], colors = [], vmin = 0, vmax = 0,width = 1):
        """Initializes Scatterplot object with the following parameters:
        x: x-axis data
        y: y-axis data
        lowerlimx: lower limit of x-axis
        lowerlimy: lower limit of y-axis
        upperlimx: upper limit of x-axis
        upperlimy: upper limit of y-axis
        sizes: size of the data points
        colors: color of the data points
        vmin: minimum value of the color map
        vmax: maximum value of the color map
        """
        self.type = type
        self.x = x
        self.y = y
        self.lowerlimx = lowerlimx
        self.lowerlimy = lowerlimy
        self.upperlimx = upperlimx
        self.upperlimy = upperlimy
        self.sizes = sizes
        self.colors = colors
        self.vmin = vmin
        self.vmax = vmax
        self.width = width
        if self.lowerlimx == None:
            self.lowerlimx = np.min(x)
        if self.lowerlimy == None:
            self.lowerlimy = np.min(y)
        if self.upperlimx == None:
            self.upperlimx = np.max(x)
        if self.upperlimy == None:
            self.upperlimy = np.max(y)
    def plot(self):
        if self.type == "s":
            """Plots the scatter plot with the given parameters"""
            fig, ax = plt.subplots()
            if(len(self.sizes) != 0 and len(self.colors) != 0):
                ax.scatter(self.x, self.y, s=self.sizes, c=self.colors, vmin=self.vmin, vmax=self.vmax)
            elif(len(self.sizes) != 0):
                ax.scatter(self.x, self.y, s=self.sizes, vmin=self.vmin, vmax=self.vmax)
            else:
                ax.scatter(self.x, self.y, s = 20, vmin=self.vmin, vmax=self.vmax)
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            ax.set(xlim=(self.lowerlimx, self.upperlimx), xticks=np.arange(self.lowerlimx+1, self.upperlimx),
            ylim=(self.lowerlimy, self.upperlimy), yticks=np.arange(self.lowerlimy+1, self.upperlimy))
            plt.show()

# make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

scatterplot1 = scatter("s",x,y,0,0,10,10,sizes,colors,0,40)
scatterplot1.plot()