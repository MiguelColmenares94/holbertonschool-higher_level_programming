#!/usr/bin/python3
if __name__ == "__main__":

    import calculator_1

    add = calculator_1.add
    sub = calculator_1.sub
    mul = calculator_1.mul
    div = calculator_1.div
    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
