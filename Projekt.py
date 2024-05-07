import numpy as np
import matplotlib . pyplot as plt


class plot:
    def __init__(self,xmin,xmax,ymin,ymax):
        plt.rcParams['toolbar'] = 'None'
        self.fig, self.ax = plt.subplots()
        self.line=[]
        
        #self.ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
        
        
        plt.show(block=False)

    def addLine(self,x,y):
        #Gammla
        plt.setp(plt.gca().lines, color="gray", linestyle="dotted", linewidth=1)

        #Nya
        line = self.ax.plot(x, y, color="black",linestyle="dotted",marker="x",markevery=[-1])

        self.line.append(line)
        plt.draw()

    def addScatter(self,x,y):
        line = self.ax.scatter(x, y)
        self.line.append(line)
        plt.draw()

    def clear(self):
        self.line=[]
        self.ax.clear()
        plt.draw()

a = plot(0,10,0,5)
a.addLine([0,1,2,3],[7,6,5,4])
a.addScatter([0,1,2,3],[1,3,1,3])
a.addLine([0,1,2,3],[1,3,1,3])
