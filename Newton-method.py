import math

#Defining Function
def f(x):
    y = (math.e) ** (6*x) + 3*(math.log(2)**2)*(math.e **(2*x)) - (math.log(8)*(math.e **(4*x))) - (math.log(2)**3)
    return y

#derivative of function
def g(x):
    g =  6*(math.e ** (6*x)) + 6*(math.log(2)**2)*(math.e**(2*x)) - 12*(math.log(2))*(math.e ** (4*x))
    return g

#Newton Method
def NewtonMethod(p0,error):
    print('\n\n----- NEWTON METHOD -----')
    print('\nP0 = %0.6f\n' % (p0))
    step = 1
    
    condition = True
    while condition:
        #check conditon
        if g(p0) == 0.0:
            print("Error : P1 cannot be computed since f'(O) = 0")
            break
        
        p1 = p0 - f(p0)/g(p0)
        print('Iteration-%d, p%d = %0.6f, f(p%d) = %0.6f and g(p%d) = %0.6f' % (step, step, p1,step, f(p1),step, g(p1)))
        p0 = p1
        step = step + 1
        
       #check accuracy
        condition = abs(f(p1)) > error
    
    print('\nThe accuracy within %f gives the approximate solution: %0.8f' % (error,p0))


#Inputs
p0 = float(input('Enter P0: '))
error = float(input('Input Error: '))


#Starting Newton Method
NewtonMethod(p0,error)
