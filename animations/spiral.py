from matplotlib import pyplot as plt
from matplotlib import animation
from math import sin, cos, pi
from physcis_systems.dynamic_spring import spring
from lin_alg_tools.lin_alg_tools import lin_space


fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw="20", marker='o')
line2, = ax.plot([], [], lw="20", marker='o', color="r")
line3, = ax.plot([], [], lw="2", color="k")
lim = 10
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
#  Plot static circle
theta = lin_space(0, 8 * pi, 200)
radius = lin_space(0, 8, 200)
a = []
b = []
shift = 3
for i in range(len(theta)):
    a.append(radius[i]*cos(theta[i]))
    b.append(radius[i]*sin(theta[i]) + shift)
ax.plot(a, b, color="k", lw="2")


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line, line2, line3


# animation function.  This is called sequentially
def animate(i):
    scaling = 1.7
    w = 0.025*scaling
    r = 8/200 * i*0.2*scaling
    a = r * cos(i * w)
    b = r * sin(i * w) + shift
    if r > radius[-1]:
        a = radius[-1]*cos(theta[-1])
        b = radius[-1]*sin(theta[-1]) + shift
    s_a, s_b = spring([a, b], [0, -8], 20, 1)

    line.set_data(a, b)
    line2.set_data(0, -8)
    line3.set_data(s_a, s_b)
    return line3, line, line2,


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=600, interval=20, blit=True)

#  anim.save('../gifs/spiral.gif', writer='imagemagick', fps=30)

plt.show()
