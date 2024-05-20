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

    while   state_vector[3] >= -1 :

        x_points = np.append(x_points,state_vector[2])

        y_points = np.append(y_points, state_vector[3])
        # This matrix computes euler forward for coordinate and velocity in x,y
        euler_matrix = np.array([[1-t*k/m,0,0,0],
                                 [0,1-t*k/m,0,0],
                                 [t,0,1,0],
                                 [0,t,0,1]])
        state_vector = np.matmul(euler_matrix,state_vector) + t*f 
        #print(state_vector)
    
    # crops to keep the last x,y pair with negative y while only.
    for i in range(len(y_points)):
        if y_points[i] < 0:
            y_points = y_points[:i]
            x_points = x_points[:i]
            break
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
        #print(state_vector)
    
    for i in range (len(y_points)):
        if y_points[i] < 0:
            y_points = y_points[:i]
            x_points = x_points[:i]
            break
    return x_points, y_points

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
    
    while abs(estimate - hit) > error/10: 
        
        if estimate < hit - error/10:
            a = c
        elif estimate > hit + error/10:
            b = c

        c = (b + a)/2
        estimate = method(c, V_y, k, m ,t)[0][-1] 
        
    return c
    
def bisect_y(hit, method, error, V_x = 0, V_y = 0, a = 0, k = 0.1, m = 10, t = 0.01):
    
    b = V_y
    c = (b + a)/2
    estimate = method(V_x, c, k ,m, t)[0][-1] 
    
    while abs(estimate - hit) > error/10: 
        
        if estimate < hit - error/10:
            a = c
        elif estimate > hit + error/10:
            b = c

        c = (b + a)/2
        estimate = method(V_x, c, k ,m ,t)[0][-1] 
        
    return c
    
    
