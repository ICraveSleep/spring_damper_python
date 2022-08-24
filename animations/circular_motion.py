from matplotlib import pyplot as plt
from matplotlib import animation
from math import sin, cos, pi
from physcis_systems.dynamic_spring import spring


def lin_space(min, max, samples):
    spaces = []
    for i in range(samples):
        temp = min + i * (max - min) / (samples - 1)
        spaces.append(temp)

    return spaces


fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw="20", marker='o')
line2, = ax.plot([], [], lw="20", marker='o', color="r")
line3, = ax.plot([], [], lw="2", color="k")
lim = 10
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
#  Plot static circle
theta = lin_space(0, 2 * pi, 100)
r = 5
a = [r * cos(t) for t in theta]  # a = r * cos(theta)
b = [r * sin(t) for t in theta]  # b = r * sin(theta)
ax.plot(a, b, color="k", lw="2")


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line, line2, line3


# animation function.  This is called sequentially
def animate(i):
    w = 0.025
    w_2 = w * 1.45
    a = r * cos(i * w)
    b = r * sin(i * w)
    c = r * cos(i * w_2 + 20)
    d = r * sin(i * w_2 + 20)
    s_a, s_b = spring([a, b], [c, d], 20, 1)

    line.set_data(a, b)
    line2.set_data(c, d)
    line3.set_data(s_a, s_b)
    return line3, line, line2,


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=600, interval=20, blit=True)

anim.save('../gifs/circular_race.gif', writer='imagemagick', fps=30)

plt.show()
