#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sylatupa
#
# Created:     20/09/2015
# Copyright:   (c) sylatupa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle

def main():
    print "here"
    fibonacci(1)
    draw_spiral()
    pass


def fibonacci(n):
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


def square(t, seg, size, fib):
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
        fib = fibonacci(i)
        if (fib>0):
            size = fib * 10  # a multiplier to give squares a reasonable size
            print "seg: ", seg, "size: ", size, "fib: ", fib

            square(t, seg, size, fib)
            seg = 5
    turtle.done()

if __name__ == '__main__':

    main()
