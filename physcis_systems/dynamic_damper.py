from math import sqrt


def damper(start: [], end: [], init_len=1, side_len=1, width=1):
    length = sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
    travel = length - 2*init_len
    u_t = [(end[0] - start[0]) / length, (end[1] - start[1]) / length]
    u_n = [(0 * u_t[0] + (-1) * u_t[1]), 1 * u_t[0] + 0 * u_t[1]]
    p_x = [start[0]]
    p_y = [start[1]]

    p_x.append(init_len*u_t[0] + start[0])
    p_y.append(init_len*u_t[1] + start[1])
    p_xm = p_x[-1]
    p_ym = p_y[-1]
    p_x.append(width*u_n[0]+p_xm + start[0])
    p_y.append(width*u_n[1]+p_ym + start[1])
    p_x.append(p_xm+width*u_n[0]+side_len*u_t[0])
    p_y.append(p_ym+width * u_n[1]+side_len*u_t[1])
    p_x.append(width * u_n[0] + p_xm)
    p_y.append(width * u_n[1] + p_ym)
    p_x.append(-width * u_n[0] + p_xm)
    p_y.append(-width * u_n[1] + p_ym)
    p_x.append(p_xm - width * u_n[0] + side_len * u_t[0])
    p_y.append(p_ym - width * u_n[1] + side_len * u_t[1])

    # back to fork line
    p_x.append(-width * u_n[0] + p_xm)
    p_y.append(-width * u_n[1] + p_ym)

    # Go to travel line
    p_x.append(-width * u_n[0] + p_xm + travel*u_t[0])
    p_y.append(-width * u_n[1] + p_ym + travel*u_t[1])

    # Create Travel line
    p_x.append(width * u_n[0] + p_xm - travel*u_n[0])
    p_y.append(width * u_n[1] + p_ym + travel * u_n[1])

    # Go to center of travel line
    p_x.append(-width * u_n[0] + p_xm + travel * u_t[0] + width*u_n[0])
    p_y.append(-width * u_n[1] + p_ym + travel * u_t[1] + width*u_n[1])

    # Go to end
    p_x.append(end[0])
    p_y.append(end[1])

    return p_x, p_y


if __name__ == "__main__":
    from matplotlib import pyplot as plt

    fig = plt.figure()
    ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    line, = ax.plot([], [], lw="20", marker='o')
    lim = 10
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    a, b = damper([-2, 0], [4, 6], side_len=4, width=1, init_len=3)
    ax.plot(a, b, color="k", lw="2")
    plt.grid()
    plt.show()
