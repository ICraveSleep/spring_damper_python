from math import sqrt, sin, cos, pi
from matplotlib import pyplot as plt
from matplotlib import animation

from lin_alg_tools.lin_alg_tools import lin_space


def four_point_rotation(start, end):
    p_x = [start[0]]
    p_y = [start[1]]
    length = sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    u_t = [(end[0] - start[0]) / length, (end[1] - start[1]) / length]
    n = 3
    step = length / n
    for i in range(1, n+1):
        p_x.append(start[0] + u_t[0]*step*i)
        p_y.append(start[1] + u_t[1]*step*i)
    return p_x, p_y


if __name__ == '__main__':
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    line, = ax.plot([], [], lw="2", marker='o')
    lim = 5
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        return line,

    # animation function.  This is called sequentially
    def animate(i):
        w = 0.025
        w_2 = w * 1.45
        r = 3
        a = r * cos(i * w)
        b = r * sin(i * w)
        c = r * cos(i * w_2 + 20)
        d = r * sin(i * w_2 + 20)
        s_a, s_b = four_point_rotation([a, b], [c, d])

        line.set_data(s_a, s_b)
        return line,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=600, interval=20, blit=True)
    # anim.save('../gifs/circular_race.gif', writer='imagemagick', fps=30)
    plt.grid()
    plt.show()
