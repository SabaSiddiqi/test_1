#https://stackoverflow.com/questions/21352580/matplotlib-plotting-numerous-disconnected-line-segments-with-different-colors

import pylab as pl
from matplotlib import collections  as mc

def display_graph(coor_list):
    
    lines=coor_list
    lc = mc.LineCollection(lines,linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.show()

    

