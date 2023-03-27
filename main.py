a = float(input("Enter a value for a (lowe limit) : "))
b = float(input("Enter a value for b:(upper limit) "))
n = float(input("Enter number of intervals "))



def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n  # width of each interval
    s = (f(a) + f(b)) / 2  # sum of first and last terms in the formula
    for i in range(1, n):
        x = a + i * h  # value of x at the midpoint of the i-th interval
        s += f(x)
    return h * s

def f(x):
    return x**2 #set your f(x)according to you fuction ,,this is for y=x**2


result = trapezoidal_rule(f, a, b, n)
print("the approximate area is ",result)
