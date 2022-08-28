from matplotlib import pyplot as plt
from matplotlib import animation
from math import sin, cos, pi
from physcis_systems.dynamic_damper import damper
from lin_alg_tools.lin_alg_tools import lin_space

fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw="20", marker='o')
line2, = ax.plot([], [], lw="20", marker='o', color="r")
line3, = ax.plot([], [], lw="2", color="k")
lim = 8
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
#  Plot static circle
theta = lin_space(-2 * pi, 2 * pi, 100)
r = 1

a = theta  # a = r * cos(theta)
b = [r * cos(t) + 2 for t in theta]  # b = r * sin(theta)
c = [5 * cos(t) for t in theta]
d = [-5] * len(theta)
ax.plot(a, b, color="k", lw="2")
ax.plot(c, d, color="k", lw="2")


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
    b = (-5)
    a = 5 * sin(i * 0.01)

    d = r * cos(i * 0.1) + 2
    c = i * 0.1 + theta[0]
    if c >= theta[-1]:
        c = 3 * theta[-1] - i * 0.1
        if c < theta[0]:
            c = i * 0.1 + 5 * theta[0]
            if c >= theta[-1]:
                c = 7 * theta[-1] - i * 0.1
                if c < theta[0]:
                    c = i * 0.1 + 9 * theta[0]

    s_a, s_b = damper([0, -4], [c, d], side_len=3, width=1, init_len=2)

    line.set_data(0, -4)
    line2.set_data(c, d)
    line3.set_data(s_a, s_b)

    return line3, line, line2,


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=600, interval=20, blit=True)

# anim.save('../gifs/wave_line.gif', writer='imagemagick', fps=30)

plt.show()
