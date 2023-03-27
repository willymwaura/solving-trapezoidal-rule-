



def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n  # width of each interval
    s = (f(a) + f(b)) / 2  # sum of first and last terms in the formula
    for i in range(1, n):
        x = a + i * h  # value of x at the midpoint of the i-th interval
        s += f(x)
    return h * s

def f(x):
    return x**2

result = trapezoidal_rule(f, 0, 1, 10)
print("the approximate area is ",result)
