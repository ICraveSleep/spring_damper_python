from matplotlib import pyplot as plt
from matplotlib import animation
from math import cos
from physcis_systems.dynamic_damper import damper

fig = plt.figure()
ax = plt.axes()
line, = ax.plot([], [], lw="20", marker='o')
line2, = ax.plot([], [], lw="20", marker='o', color="r")
line3, = ax.plot([], [], lw="2", color="k")
lim = 8
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line, line2, line3


# animation function.  This is called sequentially
def animate(i):
    r = 1.25
    b = (-6)
    a = 0
    c = a
    d = r * cos(i * 0.1) + 2
    s_a, s_b = damper([a, b], [c, d], side_len=4, width=1, init_len=3)

    line.set_data(a, b)
    line2.set_data(c, d)
    line3.set_data(s_a, s_b)

    return line3, line, line2,


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=600, interval=20, blit=True)

# anim.save('../gifs/wave_line.gif', writer='imagemagick', fps=30)

plt.show()
