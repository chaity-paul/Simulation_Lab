import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#initialize A, B, C
A = []
B = []
C = []

#initial concentration
A_initial = 1.0
B_initial = 2.0
C_initial = 0.0

#constant rate
k1 = 0.05
k2 = 0.05

#push initial value
A.append(A_initial)
B.append(B_initial)
C.append(C_initial)

total_time = 20
dt = 0.5

# Create the figure and axes for the plot
fig, ax = plt.subplots()
ax.set_xlim(0, (total_time/dt))
ax.set_ylim(0, 2.5)

# Initialize empty lists for the plot
line_A, = ax.plot([], label="A")
line_B, = ax.plot([], label="B")
line_C, = ax.plot([], label="C")


current_time = 0

def animate(i):
    global current_time, total_time
    if current_time <= total_time:
        A_next = A[-1] + (k2 * C[-1] - k1 * A[-1] * B[-1]) * dt
        B_next = B[-1] + (k2 * C[-1] - k1 * A[-1] * B[-1]) * dt
        C_next = C[-1] + (2 * k1 * A[-1] * B[-1] - 2 * k2 * C[-1]) * dt
        A.append(A_next)
        B.append(B_next)
        C.append(C_next)
        current_time += dt

    line_A.set_data(range(len(A)), A)
    line_B.set_data(range(len(B)), B)
    line_C.set_data(range(len(C)), C)

# Create a Animation object
animation = FuncAnimation(fig, animate, frames=1000, interval=1, repeat=False)

plt.legend()
plt.show()

print(len(A))
print(len(B))
