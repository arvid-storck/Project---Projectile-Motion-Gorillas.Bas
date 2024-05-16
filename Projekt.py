import numpy as np
import matplotlib . pyplot as plt
import math


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


import numpy as np
import matplotlib.pyplot as plt
#(x speed when t=0,y speed when t=0,k,m,steglängd)
def euler_f(v_x,v_y,k,m,t):
    
    g = 9.8
    
    A = np.array([[-k/m,0,0,0],[0,-k/m,0,0],[1,0,0,0],[0,1,0,0]]) # differentiation matrix
    f = np.array([0,-g,0,0])
    state_vector = np.array([v_x,v_y,0,0]) #speed c, speed y, x loc, y loc
    #print(state_vector)
    x_points = np.array([])
    y_points = np.array([])
    counter = 5
    itera = 0
    while   state_vector[3] >= 0 :
        itera += 1
        x_points = np.append(x_points,state_vector[2])

        y_points = np.append(y_points, state_vector[3])
        # This matrix computes euler forward for coordinate and velocity in x,y
        euler_matrix = np.array([[1-t*k/m,0,0,0],
                                 [0,1-t*k/m,0,0],
                                 [t,0,1,0],
                                 [0,t,0,1]])
        state_vector = np.matmul(euler_matrix,state_vector) + t*f 
        #print(state_vector)
        counter = counter -1 

    
    return x_points, y_points, itera


def euler_b(v_x,v_y,k,m,t):
    
    g = 9.8
    
    A = np.array([[-k/m,0,0,0],[0,-k/m,0,0],[1,0,0,0],[0,1,0,0]]) # differentiation matrix
    f = np.array([0,-g,0,0])
    state_vector = np.array([v_x,v_y,0,0]) #speed c, speed y, x loc, y loc
    #print(state_vector)
    x_points = np.array([])
    y_points = np.array([])
    counter = 5
    itera = 0
    while   state_vector[3] >= 0 :
        itera += 1
        x_points = np.append(x_points,state_vector[2])
        y_points = np.append(y_points, state_vector[3])
        # This matrix computes euler backward for coordinate and velocity in x,y
        euler_matrix = np.array([[1/(1+t*k/m),0,0,0],
                                 [0,1/(1+t*k/m),0,0],
                                 [t/(1+t*k/m),0,1,0],
                                 [0,t/(1+t*k/m),0,1]])
        state_vector = np.matmul(euler_matrix,state_vector) + t*f 
        #print(state_vector)
        counter = counter -1 

    
    return x_points, y_points, itera



"""
euler backward:
x_1 = x + t * (v_x+1)
v_x+1 = v_x + t(a_x+1)
a_x+1 = -k/m*v_x+1

=>

v_x+1 = v_x + t (-k/m * v_x+1)
= v_x+1 + t*k *vx_+1 /m = v_x
v_x+1 * (1 + t*k/m) = v_x
v_x+1 = v_x/(1+t*k/m)

x_1 = x + t * (v_x/(1+t*k/m)) 

"""



def aime(estimate,amplitude,k,m,goal,margin): #funkar inte
    h=0.01
    
    low=0
    high=90
    
    
    x_low,y=estimate(amplitude*math.cos(math.radians(low)),amplitude*math.sin(math.radians(low)),k,m,h)
    x_lowDiff=(x_low[-1]-goal)
    
    x_high,y=estimate(amplitude*math.cos(math.radians(high)),amplitude*math.sin(math.radians(high)),k,m,h)
    x_highDiff=(x_high[-1]-goal)

    if x_lowDiff>=margin and x_lowDiff<=(goal+margin):
        return high
    if x_low[-1]>=(goal-margin) and x_low[-1]<=(goal+margin):
        return low

    i=0
    while i<40:
        mid=(high+low)/2
        
        x_mid,y=estimate(amplitude*math.cos(math.radians(mid)),amplitude*math.sin(math.radians(mid)),k,m,h)
        x_midDiff=(x_mid[-1]-goal)
        #testa mid
        if x_midDiff>=-margin and x_midDiff<=margin:
            return mid

        #bifeciton
        
        
        i+=1
    #Lyckas inte hitta!
    return None

def menu():
    method=int(input("What method? 1 = euler forward, 2= euler backwards:  "))
    hit=float(input("Mål: "))
    k=float(input("k: "))
    m=float(input("m: "))
    margins=float(input("marginal: "))
    if method==1:
        gameInit(euler_f,hit,k,m,margins,0.01)
    elif method==2:
        gameInit(euler_b,hit,k,m,margins,0.01)
    
def gameInit(estimate,hit,k,m,margins,h): #estimate är uppskattningen med estimate(x speed when t=0,y speed when t=0,k,m,steglängd)

    
    a=plot(-1,hit*1.5,-1,hit)
    a.addScatter([0],[0])
    a.addLine([-1,hit*1.5],[0,0],"black")
    a.addLine([hit-margins,hit+margins],[0,0],"black",2,[-1,0])

    while True:
        amplitude=float(input("\namplitud: "))
        #angel=aime(estimate,amplitude,k,m,b,hit)#estimate,amplitude,k,m,goal,margin
        angel=input("vinkel grader: ")
        try:
            angel=math.radians(float(angel))
        except:
            print("Kan inte konvergera",angel,"till en siffra.")
            continue
        
        
        x,y,itera=estimate(amplitude*math.cos(angel),amplitude*math.sin(angel),k,m,h)
    
        a.addLine(x,y,"green","x",[-1])
    
        if (hit-margins<=x[-1]<=hit+margins):
            print("you win!")
            break

menu()
    
