#!/usr/bin/python3
if __name__ == "__main__":

    import calculator_1 as mod

    add = mod.add
    sub = mod.sub
    mul = mod.mul
    div = mod.div
    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
