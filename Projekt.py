import numpy as np
import matplotlib . pyplot as plt
import math


class plot:
    def __init__(self,xmin,xmax,ymin,ymax):
        plt.rcParams['toolbar'] = 'None'
        self.fig, self.ax = plt.subplots()
        self.line=[]
        self.ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
        self.show()
        
        

    def addLine(self,x,y,color,markers=None,markwhere=None,linestyle="solid",wait=0.5):
        #Gammla
        plt.setp(plt.gca().lines[2:], color="gray", linestyle="dotted", linewidth=1)

        #Nya
        line = self.ax.plot(x, y, color=color ,marker=markers,markevery=markwhere,linestyle=linestyle)

        self.line.append(line)
        plt.draw()
        plt.pause(wait)

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




def euler_forward_y(f,v_0,h):#Använd inte
    t_n = 0
    v_n = v_0
    
    integrate = 0#in

    #Plot stuff
    v=[v_0]

    y=[0]#in

    i=0#in
    
    while integrate>=0:#in
        v_n = v_n + h * f(v_n,t_n)
        t_n = t_n + h
        
        v.append(v_n)

        integrate += h*(v[i+1]+v[i])/2#in
        i += 1#in
        y.append(integrate)#in

    return y

def euler_forward_x(f,v_0,h,N):#Använd inte
    t_n = 0
    v_n = v_0
    
    integrate = 0#in
    
    #Plot stuff
    v=[v_0]
    
    x=[0]#in

    
    for i in range(N-1):
        v_n = v_n + h * f(v_n,t_n)
        t_n = t_n + h
        
        #Plot stuff
        v.append(v_n)

        
        integrate += h*(v[i+1]+v[i])/2#in
        x.append(integrate)#in
    return x

def euler_forward(vx,vy,k,m,h): #Inte för 2.3 men 2.5 funkar
    y = euler_forward_y((lambda v,t:-k/m*v-9.82),vy,h) #-k/m*v-g
    x = euler_forward_x((lambda v,t:-k/m*v),vx,h,len(y)) #-k/m*v-g
    return x,y



def gameInit(estimate): #estimate är uppskattningen med x,y=estimate(x speed when t=0,y speed when t=0,k,m,steglängd)
    b=float(input("Mål: "))
    k=float(input("k: "))
    m=float(input("m: "))
    hit=float(input("marginal: "))

    
    a=plot(-1,b*1.5,-1,b)
    a.addScatter([0],[0])
    a.addLine([-1,b*1.5],[0,0],"black")
    a.addLine([b-hit,b+hit],[0,0],"black",2,[-1,0])

    
    while True:
        vx=float(input("x hastighet: "))
        vy=float(input("y hastighet: "))
        print()

        #Sätt x,y uppskattningen här!
        x,y=estimate(vx,vy,k,m,0.01)
    
        a.addLine(x,y,"green","x",[-1])
    
    
        if (b-hit<=x[-1]<=b+hit):
            print("you win!")
            a.clear()
            plt.close()
            break

gameInit(euler_forward)
    
