import numpy as np
import matplotlib . pyplot as plt
import math


class plot:
    def __init__(self,xmin,xmax,ymin,ymax):
        plt.rcParams['toolbar'] = 'None'
        self.fig, self.ax = plt.subplots()
        self.line=[]
        
        self.ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
        
        
        

    def addLine(self,x,y):
        #Gammla
        plt.setp(plt.gca().lines, color="gray", linestyle="dotted", linewidth=1)

        #Nya
        line = self.ax.plot(x, y, color="green",marker="x",markevery=[-1])

        self.line.append(line)
        plt.draw()
        plt.pause(0.1)

    def addScatter(self,x,y):
        line = self.ax.scatter(x, y)
        self.line.append(line)
        plt.draw()
        plt.pause(0.01)

    def clear(self):
        self.line=[]
        self.ax.clear()
        plt.draw()
        plt.pause(0.01)

    def show(self):
        plt.show(block=False)
        plt.pause(0.01)

#a = plot(0,10,0,5)
#a.addLine([0,1,2,3],[7,6,5,4])
#a.addScatter([0,1,2,3],[1,3,1,3])
#a.addLine([0,1,2,3],[1,3,1,3])

def euler_forward_x(f,v_0,h,T):#Undersskattar värdet!
    t_n = 0
    v_n = v_0
    x_tot = 0
    h = math.copysign(h,T)
    
    #Plot stuff
    t=[0]
    v=[v_0]
    x=[0]

    
    for i in range(math.ceil(abs(T/h))):
        v_n = v_n + h * f(v_n,t_n)
        t_n = t_n + h
        
        #Plot stuff
        t.append(t_n)
        v.append(v_n)

        
        x_tot += h*(v[i+1]+v[i])/2
        x.append(x_tot)
    return x

def euler_forward_y(f,v_0,h,y_0):#Undersskattar värdet!
    t_n = 0
    v_n = v_0
    y_tot = y_0

    #Plot stuff
    t=[0]
    v=[v_0]
    y=[y_0]

    i=0
    while y_tot>0:
        v_n = v_n + h * f(v_n,t_n)
        t_n = t_n + h
        
        #Plot stuff
        t.append(t_n)
        v.append(v_n)

        i += 1
        y_tot += h*(v[i]+v[i-1])/2
        y.append(y_tot)

    return t_n,y

b=float(input("Mål: "))
a=plot(-b/5,b*1.5,-1,b)
a.addScatter([b],[0])
while True:
    vx=float(input("x hastighet: "))
    vy=float(input("y hastighet: "))
    print()
    
    t,y = euler_forward_y(lambda v,t:-1/1*v-9.82,vy,0.01,2) #-k/m*v-g
    
    x = euler_forward_x(lambda v,t:-1*v,vx,0.01,t)# -k/m*v
    
    print(len(x),len(y))
    
    a.addLine(x,y)
    
