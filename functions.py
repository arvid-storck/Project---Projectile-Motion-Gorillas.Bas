import numpy as np
import matplotlib . pyplot as plt
import math

def euler_f(v_x,v_y, k = 0.1, m = 10, t = 0.01):
    
    g = 9.8
    f = np.array([0,-g,0,0])
    state_vector = np.array([v_x,v_y,0,0]) #speed c, speed y, x loc, y loc
    #print(state_vector)
    x_points = np.array([])
    y_points = np.array([])

    while  state_vector[3] >= 0 :

        x_points = np.append(x_points,state_vector[2])

        y_points = np.append(y_points, state_vector[3])
        # This matrix computes euler forward for coordinate and velocity in x,y
        euler_matrix = np.array([[1-t*k/m,0,0,0],
                                 [0,1-t*k/m,0,0],
                                 [t,0,1,0],
                                 [0,t,0,1]])
        state_vector = np.matmul(euler_matrix,state_vector) + t*f 
        #print(state_vector)
    
    return x_points, y_points


def euler_b(v_x,v_y, k = 0.1, m = 10, t = 0.01):
    
    g = 9.8
    f = np.array([0,-g,0,0])
    state_vector = np.array([v_x,v_y,0,0]) #speed c, speed y, x loc, y loc
    #print(state_vector)
    x_points = np.array([])
    y_points = np.array([])

    while   state_vector[3] >= 0 :

        x_points = np.append(x_points,state_vector[2])
        y_points = np.append(y_points, state_vector[3])
        # This matrix computes euler backward for coordinate and velocity in x,y
        euler_matrix = np.array([[1/(1+t*k/m),0,0,0],
                                 [0,1/(1+t*k/m),0,0],
                                 [t/(1+t*k/m),0,1,0],
                                 [0,t/(1+t*k/m),0,1]])
        state_vector = np.matmul(euler_matrix,state_vector) + t*f
    return x_points, y_points

#This funktions assume that given a the value V_x (or V_y) that x_points[-1] will hit at or past the taget with the value V_y=1000 (V_x=1000)
#If V_x=0.0001, will any values of V_y make x_points[-1] converge to the taget?
#If the error is low then we can get problems with rounding errors, but that will happen with any use of the bisektion method
#Another way could be to use angels. Angels will work since we have an minimum and an maximum.
#Just have to check if it will reach the taget at all this can be done.
#Changing both speed values will work since increasing the speed equaly will hit given its fast enough.
def aim_assist(hit, method, error,V_x = 0,V_y = 0, k = 0.1, m = 10, t = 0.01):
    
    if V_x == 0:

        estimate = bisect_x(hit, method, error,V_x = 1000, V_y = V_y)
    else:

        estimate = bisect_y(hit, method, error, V_x = V_x, V_y = 1000)
        
    return estimate
         
def bisect_x(hit, method, error, V_x = 0, V_y = 0, a = 0, k = 0.1, m = 10, t = 0.01):
    
    b = V_x
    c = (b + a)/2
    estimate = method(c, V_y, k, m ,t)[0][-1] 

    i=0
    while abs(estimate - hit) > error/10 and i<100: 
        
        if estimate < hit - error/10:
            a = c
        elif estimate > hit + error/10:
            b = c

        c = (b + a)/2
        estimate = method(c, V_y, k, m ,t)[0][-1] 

        i+=1
    return c
    
def bisect_y(hit, method, error, V_x = 0, V_y = 0, a = 0, k = 0.1, m = 10, t = 0.01):
    
    b = V_y
    c = (b + a)/2
    estimate = method(V_x, c, k ,m, t)[0][-1] 

    i=0
    while abs(estimate - hit) > error/10 and i<100: 
        
        if estimate < hit - error/10:
            a = c
        elif estimate > hit + error/10:
            b = c

        c = (b + a)/2
        estimate = method(V_x, c, k ,m ,t)[0][-1]

        i+=1
        
    return c
    
    
