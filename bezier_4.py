import matplotlib.pyplot as plt
def factorial(n):
    ans = 1
    for i in range(1 , n + 1):
        ans *= i
    return ans
def nCr(n , r):
    return factorial(n) / float(factorial(r) * factorial(n - r))

def BEZ(n, i , t):
    result = nCr(n, i) * (t ** i) * (1 - t) ** (n - i)
    return result

def bezier_curve(x_c_p, y_c_p):
    n = len(x_c_p) - 1
    esp = 0.01
    t = 0
    x_curve = []
    y_curve = []

    end = 1.01
    while t < end:
        x = 0
        y = 0

        for i in range(0, n + 1):
            bez = BEZ(n, i, t)
            x += x_c_p[i] * bez
            y += y_c_p[i] * bez
        
        x_curve.append(x)
        y_curve.append(y)

        plt.clf()
        plt.title("Bezier curve")
        plt.plot(x_c_p, y_c_p, label = "control point")
        plt.plot(x_curve, y_curve, label ="bezier curve")
        plt.legend()
        plt.grid()
        plt.pause(0.001)
        t += esp
    plt.show()

x_control_point = [1 , 17, 15 , 21]
y_control_point = [5, 10, 5 , 10]
bezier_curve(x_control_point,y_control_point)