a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
def findint(a, b, c, d, e, f):
    for x in range(-10, 11):
        for y in range(-10, 11):
            if a * x + b * y == c and d * x + e * y == f:
                return x, y
    return None
int1 = [a, b, c, d, e, f]
solution = findint(*int1)

if solution:
    x, y = solution
    print(x , y)
else:
    print("No solution")