#!/usr/bin/python3


for tebahpla in range(122, 96, -1):
    
    if tebahpla % 2 == 0:
        pass
    elif tebahpla % 2 == 1:
        tebahpla -= 32
    
    print("{:c}".format(tebahpla), end="")
