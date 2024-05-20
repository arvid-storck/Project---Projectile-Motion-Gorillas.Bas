import matplotlib . pyplot as plt
import math
from functions import aim_assist, euler_f, euler_b

def main():
    
    target = 30
    k = 0.1
    m = 10
    t = 0.01
    error_margin = 1
    
    method_choice = input(
        "Choose the method\nFor euler forward enter 1\nFor euler backwards enter 2\n")

    
    if method_choice == "1":
        algoritm = euler_f
    elif method_choice == "2":
        algoritm = euler_b
    else:
        print("Not a valid input for method")
        return None
    try:
        V_x = float(input("Enter the first speed vector Vx: ").strip())
        V_y = float(input("Enter the second speed vector Vy: ").strip())
    except:
        print("Failed at converting to float")
    
    x,y = algoritm(V_x, V_y, k, m, t)
    plt.axhline(0,color='black')
    plt.plot(target, 0, 'ro')
    plt.plot(x,y,marker="3",markevery=[-1])
    plt.show()
    
    if error_margin > abs(target - x[-1]):
        print("You won!")
    else:
        input_2 = input("\nYou missed,\ntype 1 to get a suggestion for a better Vx value\n"+
                        "type 2 for a better Vy value\n" \
                        +"type 3 to exit\n")
        if input_2 == "1":
            print("\nChoose Vx to :" + str(aim_assist(target,
                                                    algoritm,
                                                    error_margin,
                                                    V_y = V_y, 
                                                    k= k, 
                                                    m=m, 
                                                    t=t)))
        elif input_2 == "2":
            print("\nChoose Vy to :"+ str(aim_assist(target,
                             algoritm,
                             error_margin,
                             V_x = V_x,
                             k= k, 
                             m=m, 
                             t=t)))
        else:
            print("\nGoodbye!")

main()
