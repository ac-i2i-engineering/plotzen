import matplotlib.pyplot as plt
import numpy as np
import scatterplot
import linegraph
import baro

class Plot:
    def Plot(type, x, y, lowerlimx, lowerlimy, upperlimx, upperlimy, sizes = [], colors = [], vmin = 0, vmax = 0, width = 1):
        plt.style.use('_mpl-gallery')
        if type == "scatter":
            scatterplot.scatter.run(x, y, lowerlimx, lowerlimy, upperlimx, upperlimy, sizes, colors, vmin, vmax)
        if type == "multi-line":
            linegraph.line.run(x, y, lowerlimx, lowerlimy, upperlimx, upperlimy, width)
        if type == "bar":
            baro.easybar(x, y, upperlimx, upperlimy, width)

# make the data
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))
Plot.plot("scatter",x,y,0,0,10,10,sizes,colors,0,40)
       
            