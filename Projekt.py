import numpy as np
import matplotlib . pyplot as plt
import math
import random


class plot:
    def __init__(self,xmin,xmax,ymin,ymax):
        #plt.rcParams['toolbar'] = 'None'
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


def aime(estimate,amplitude,k,m,goal,margin):
    h=0.01
    
    low=0
    high=90
    mid=(high+low)/2
    
    
    x_low,y=estimate(amplitude*math.cos(math.radians(low)),amplitude*math.sin(math.radians(low)),k,m,h)
    x_lowDiff=(x_low[-1]-goal)
    
    x_high,y=estimate(amplitude*math.cos(math.radians(high)),amplitude*math.sin(math.radians(high)),k,m,h)
    x_highDiff=(x_high[-1]-goal)

    if x_lowDiff>=margin and x_lowDiff<=(goal+margin):
        return high
    if x_low[-1]>=(goal-margin) and x_low[-1]<=(goal+margin):
        return low

    #Find positive value for x[-1]-goal
    
    i=0
    while i<40:
        x_mid,y=estimate(amplitude*math.cos(math.radians(mid)),amplitude*math.sin(math.radians(mid)),k,m,h)
        x_midDiff=(x_mid[-1]-goal)
        
        #testa mid
        if x_midDiff>-margin and x_midDiff<margin:
            return mid

        #bifeciton
        if (x_midDiff)*(x_lowDiff)<0:
            high=mid
            x_highDiff=x_midDiff
        else:
            low=mid
            x_lowDiff=x_midDiff
            
        mid=(high-low)/2
        i+=1
    #Lyckas inte hitta!
    print("miss!")
    return random.random()*180
    

def gameInit(estimate,h): #estimate är uppskattningen med estimate(x speed when t=0,y speed when t=0,k,m,steglängd)
    b=float(input("Mål: "))
    k=float(input("k: "))
    m=float(input("m: "))
    hit=float(input("marginal: "))
    print()
    
    a=plot(-1,b*1.5,-1,b)
    a.addScatter([0],[0])
    a.addLine([-1,b*1.5],[0,0],"black")
    a.addLine([b-hit,b+hit],[0,0],"black",2,[-1,0])

    while True:
        amplitude=float(input("amplitud: "))
        angel=aime(estimate,amplitude,k,m,b,hit)#estimate,amplitude,k,m,goal,margin
        print(angel)
        try:
            angel=math.radians(angel)
            #angel=math.radians(float(input("vinkel grader: ")))
        except:
            print("Flyttals fel")
            continue
        print()
        
        x,y=estimate(amplitude*math.cos(angel),amplitude*math.sin(angel),k,m,h)
    
        a.addLine(x,y,"green","x",[-1])
    
        if (b-hit<=x[-1]<=b+hit):
            print("you win!")
            #a.clear()
            #plt.close()
            break

gameInit(euler_forward,0.001)
    
