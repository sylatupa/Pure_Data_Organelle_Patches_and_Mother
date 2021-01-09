#fib
import turtle
"""
draw_spiral() uses the Turtle to draw an approximation of the Golden Spiral, using
a Fibonacci series
"""

def __fibonacci(n):
    fib1 = 0; fib2 = 1
    if n == 0:
        return fib1
    elif n == 1:
        return fib2
    else:
        for i in range(n-1):
            fib = fib1 + fib2
            fib1, fib2 = fib2, fib
        return fib


def __square(t, seg, size, fib):
    """
    takes a turtle, number of segments, and a side dimension (size)
    """
    for i in range(seg):
        t.fd(size)
        t.left(90)
    t.write(fib)# write the current Fibonacci number next to the square
    t.fd(size)


def draw_spiral(size=10):
    t = turtle.Turtle()
    seg = 3 # set to 5 segments after first pass
    for i in range(size):
        fib = __fibonacci(i)
        if (fib>0):
            size = fib * 10  # a multiplier to give squares a reasonable size
            __square(t, seg, size, fib)
            seg = 5
    turtle.done()

draw_spiral()
