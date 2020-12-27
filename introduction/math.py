import math

# print(math.pi)

a = 529
b = 148
# print('addition', a+b)
# print('substraction', a-b)
# print('mult', a*b)
# print('division', a/b)
# print('division without decimals', a//b)
# print('division rest', a % b)

# calculate circle area


def circleArea(radius):
    # check radius
    if (isinstance(radius, (int, float))):
        if (radius < 0):
            return ValueError('radius cannot be negative')
        return math.pi * radius * radius
    return ValueError('radius can only be positive int or float')


print(circleArea(8.2545))
