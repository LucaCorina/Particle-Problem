import math

class Function :
    def __int__(self):
        self.__index = 0
'''
    * Calculate the result of (x^4)-2(x^3).
    * Domain is (-infinity, infinity).
    * Minimum is -1.6875 at x = 1.5.
    * @param x     the x component
    * @return      the y component
'''
def functionA ( x) :
    return math.pow(x, 4) - 2 * math.pow(x, 3);


'''
 * Perform Ackley's function.
 * Domain is [5, 5]
 * Minimum is 0 at x = 0 & y = 0.
 * @param x     the x component
 * @param y     the y component
 * @return      the z component
'''
def ackleysFunction ( x,  y) :
    p1 = -20*math.exp(-0.2*math.sqrt(0.5*((x*x)+(y*y))));
    p2 = math.exp(0.5*(math.cos(2*math.PI*x)+math.cos(2*math.PI*y)));
    return p1 - p2 + math.E + 20;

