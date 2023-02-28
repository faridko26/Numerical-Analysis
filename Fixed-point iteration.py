
import math

# f(x)
def f(x):
    y = 3*(x**2) - math.exp(x)
    return y

# g(x)
def g(x):
    return ((math.exp(x))/3)**0.5

# Fixed Point Iteration Method
def fixedPointIteration(p0, e):
    
    step = 1
    condition = True
    while condition:
        p1 = g(p0)
        print('Iteration-%d :   p%d = %0.6f ----> f(p%d) = %0.6f' % (step, step, p1, step, f(p1)))
        p0 = p1

        step = step + 1

        condition = abs(f(p1)) > e

   
    print('\nThe accuracy within %f gives the approximate solution: %0.8f' % (e,p1))
   



#input
p0 = float(input('Enter Initial approx: '))
e = float(input('Error: '))

# Starting
print('\n\n----- FIXED POINT ITERATION -----')
fixedPointIteration(p0,e)
