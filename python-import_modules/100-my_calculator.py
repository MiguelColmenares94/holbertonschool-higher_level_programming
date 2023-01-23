#!/usr/bin/python3
if __name__ == "__main__":

    import calculator_1
    from sys import argv, exit

    a = int(argv[1])
    b = int(argv[3])
    c = argv[2]
    mod = calculator_1

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if c == "+":
        print("{:d} {} {:d} = {:d}".format(a, c, b, mod.add(a, b)))
        exit(0)
    elif c == "-":
        print("{:d} {} {:d} = {:d}".format(a, c, b, mod.sub(a, b)))
        exit(0)
    elif c == "*":
        print("{:d} {} {:d} = {:d}".format(a, c, b, mod.mul(a, b)))
        exit(0)
    elif c == "/":
        print("{:d} {} {:d} = {:d}".format(a, c, b, mod.div(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
