import math as m

# Function
def f(x):
    y = x - 2*m.sin(x)
    return y

# Bisection Method
def bisection(a1,b1,error):
    step = 1
    condition = True
    while condition:
        p1 = (a1 + b1)/2
        print('Iteration-%d :   p%d = %0.6f ----> f(p%d) = %0.6f' % (step, step, p1, step, f(p1)))

        if f(a1) * f(p1) < 0:
            b1 = p1
        else:
            a1 = p1
        
        condition = abs(f(p1)) > error
        step = step + 1

    print('\nThe accuracy within %f gives the approximate solution: %0.8f' % (error,p1))


#Input
a1 = float(input('lower bound: '))
b1 = float(input('upper bound: '))
error = float(input('Error: '))


# Checking condition of bisection method
if f(a1) * f(b1) > 0.0:
    print('The interval do not bracket the root.')
    print('Try Again with different interval.')
else:
    print('\n\n----- BISECTION METHOD -----')
    bisection(a1,b1,error)
