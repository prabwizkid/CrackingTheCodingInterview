# Given a number of base 10 (Decimal), return the base 2 equivalent (Binary)

import math


def getBinary(n, binary):
    power = int(str(math.log(n, 2)).split(".")[0])
    n = n - math.pow(2, power)
    binary[power] = 1
    if n == 0.0:
        return "".join([str(c) for c in binary[::-1]])
    else:
        return getBinary(n, binary)


if __name__ == "__main__":
    n = 75
    power = int(str(math.log(n, 2)).split(".")[0])
    binary = [0] * (power + 1)
    print(getBinary(n, binary))


