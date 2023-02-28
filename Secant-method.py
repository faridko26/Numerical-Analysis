import math

# Defining Function
def f(x):
    y = (x - 2)**2 - math.log(x)
    return y

#Secant Method
def secant(p0,p1,error):
    print('\n\n----- SECANT METHOD -----')
    print('Iteration- 0, p0 = %0.6f and f(p0) = %0.6f' % (p0, f(p0)))
    print('Iteration- 1, p1 = %0.6f and f(p1) = %0.6f' % (p1, f(p1)))
    step = 2
    condition = True
    while condition:
        if f(p0) == f(p1):
            print('Divide by zero error!')
            break
        #Calculate f(p1) to check the absolute error
        h = f(p1)
        
        p2 = p0 - (p1-p0)*f(p0)/( f(p1) - f(p0) ) 
        print('Iteration-%d, p%d = %0.6f and f(p%d) = %0.6f' % (step,step, p2,step, f(p2)))
        p0 = p1
        p1 = p2
        step = step + 1
        
        if step > 1000:
            print('After 1000 Iteration it is Not Convergent!')
            break
        
        condition = abs(f(p2)-h) > error
    print('\nThe accuracy within %f gives the approximate solution: %0.8f' % (error,p2))


#Inputs
p0 = float(input('Enter First Guess: '))
p1 = float(input('Enter Second Guess: '))
error = float(input('Enter Error: '))


# Starting Secant Method
secant(p0,p1,error)
