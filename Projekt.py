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
        plt.pause(1)

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



def euler_forward_y(f,t_0,v_0,h,y_0):#Undersskattar värdet!
    t_n = t_0
    v_n = v_0
    
    integrate = y_0#in

    #Plot stuff
    t=[t_0]
    v=[v_0]

    y=[y_0]#in

    i=0#in
    
    while integrate>=0:#in
        v_n = v_n + h * f(v_n,t_n)
        t_n = t_n + h
        
        t.append(t_n)
        v.append(v_n)

        integrate += h*(v[i+1]+v[i])/2#in
        i += 1#in
        y.append(integrate)#in

    return t,v,y

def euler_forward_x(f,t_0,v_0,h,x_0,N):#Undersskattar värdet!
    t_n = t_0
    v_n = v_0
    
    integrate = 0
    
    #Plot stuff
    t=[0]
    v=[v_0]
    
    x=[x_0]#in

    
    for i in range(N-1):
        v_n = v_n + h * f(v_n,t_n)
        t_n = t_n + h
        
        #Plot stuff
        t.append(t_n)
        v.append(v_n)

        
        integrate += h*(v[i+1]+v[i])/2#in
        x.append(integrate)#in
    return t,v,x

b=float(input("Mål: "))
k=float(input("k: "))
m=float(input("m: "))
a=plot(-1,b*1.5,-1,b)
a.addScatter([b],[0])
while True:
    vx=float(input("x hastighet: "))
    vy=float(input("y hastighet: "))
    print()
    
    t,v,y = euler_forward_y((lambda v,t:-k/m*v-9.82),0,vy,0.01,2) #-k/m*v-g
    
    t,v,x = euler_forward_x((lambda v,t:-k/m*v),0,vx,0.01,0,len(y)) #-k/m*v-g
    
    a.addLine(x,y)
    
    hit=2
    if (b-hit<=x[-2]<=b+hit):
        print("you win!")
        break
    
