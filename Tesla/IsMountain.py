# Given an array of integers arr, return true if and only if it is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


def isMountain(arr):
    peak, valley, plain = 0, 0, 0
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            peak += 1
            print(peak)
        if arr[i - 1] >= arr[i] <= arr[i + 1]:
            valley += 1
            print(valley)
        if arr[i - 1] < arr[i] >= arr[i + 1]:
            plain += 1
            print(plain)
            # print(i)
    return peak == 1 and valley == 0


def isM(arr):
    isinc, isdec, isconst = 1, 1, 1
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i]:
            isinc = 0
        elif arr[i - 1] == arr[i]:
            isconst = 1
        elif arr[i - 1] > arr[i]:
            isdec = 2

    if isinc < isconst < isdec:
        return True
    else:
        return False

# Doesnt work for plains
# print(isMountain([1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 0]))

print(isM([1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 0]))
print(isM([1, 2, 3, 4, 5, 4, 3, 2, 1, 0]))

# Doesnt work for 2 mountains
print(isM([1, 2, 3, 2, 1, 2, 3, 2, 1]))


