from matplotlib import pyplot as plt
from matplotlib import animation
from physcis_systems.dynamic_spring import spring
from physcis_systems.dynamic_damper import damper
import numpy as np
from numpy.linalg import inv
from lin_alg_tools.lin_alg_tools import lin_range

if __name__ == '__main__':
    # TODO Clean up this abomination of a code
    def compress(x, time, fps):
        x_new = [x[0]]
        time_new = [time[0]]
        compress_value = 1 / fps
        counter = 0
        for i in time:
            if i > compress_value:
                x_new.append(x[counter])
                time_new.append(time[counter])
                compress_value += 1 / fps
            counter += 1
        return x_new, time_new

    # Animation
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    line3, = ax.plot([], [], lw="2", color="k")
    line4, = ax.plot([], [], lw="2", color="k")
    box, = ax.plot([], [], linestyle='None', marker='s', markersize=60, markeredgecolor='k', color='orange',
                   markeredgewidth=2)
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
    lim = 14
    lim_shift = 5
    x_lim = 7
    ax.set_xlim(-x_lim, x_lim)
    ax.set_ylim(-lim + lim_shift, lim + lim_shift)
    ax.plot([-lim, lim], [12, 12], lw="2", color="k")

    # Dynamics
    m = 2
    k = 2
    d = 0.2
    F_0 = 0
    dt = 0.01
    time = lin_range(0.0, 20.0, dt)
    y = np.array([0, 1.5])  # [init_velocity, init_displacement]
    A = np.array([[m, 0], [0, 1]])
    A_inv = inv(A)
    B = np.array([[d, k], [-1, 0]])
    F = np.array([0, 0])
    #Simulation
    sim = [y[0]]
    for t in time:
        y = y + dt * A_inv.dot(F - B.dot(y))
        sim.append(y[0])
    sim, time = compress(sim, time, 30)
    # initialization function: plot the background of each frame
    def init():
        line3.set_data([], [])
        line4.set_data([], [])
        box.set_data([], [])
        time_text.set_text('')
        return line3, line4, box, time_text

    # animation function.  This is called sequentially
    def animate(i):

        r = 1.25
        b = 12
        a = 0
        c = a
        d = sim[i]
        shift = 0.75
        s_a, s_b = spring([a + shift, b], [c + shift, d], coils=20, width=1, init_len=1)
        s_c, s_d = damper([a - shift, b], [c - shift, d], side_len=4.5, width=0.5, init_len=4.5)

        line3.set_data(s_a, s_b)
        line4.set_data(s_c, s_d)
        box.set_data(c, d - 2.15)
        time_text.set_text(time_template % time[i])
        return line3, line4, box, time_text

    interval = 20
    print(len(time))
    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=len(time), interval=interval, blit=True)

    #anim.save('gifs/spring_damper.gif', writer='imagemagick', fps=30)

    plt.show()
