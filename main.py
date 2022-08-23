import matplotlib.pyplot as plt
from math import sqrt


def spring(start, end, elbows, width, init_lint=2):
    r_start = start
    r_end = end
    n = elbows
    r_s = []
    length = sqrt((r_end[0] - r_start[0]) ** 2 + (r_end[1] - r_start[1]) ** 2)
    u_t = [(r_end[0] - r_start[0]) / length, (r_end[1] - r_start[1]) / length]
    u_n = [(0 * u_t[0] + (-1) * u_t[1]), 1 * u_t[0] + 0 * u_t[1]]
    w = width

    for i in range(1, n + 1):
        r_x = r_start[0] + length / (2 * n) * (2 * i - 1) * u_t[0] + 0.5 * sqrt(w ** 2 - (length ** 2 / n ** 2)) * (
            -1) ** i * u_n[0]
        r_y = r_start[1] + length / (2 * n) * (2 * i - 1) * u_t[1] + 0.5 * sqrt(w ** 2 - (length ** 2 / n ** 2)) * (
            -1) ** i * u_n[1]
        r_i = [r_x, r_y]
        r_s.append(r_i)

    if init_lint <= 0:
        r1 = [r_start[0]]
        r2 = [r_start[1]]

    else:
        print("AYO")
        r1 = [r_start[0]]
        r2 = [r_start[1]]
    for r in r_s:
        r1.append(r[0])
        r2.append(r[1])
    r1.append(r_end[0])
    r2.append(r_end[1])
    return r1, r2


if __name__ == '__main__':
    n = 12
    r_0 = [1, 0]
    r_9 = [-1.5, 14.8]
    r_a, r_b = spring(r_0, r_9, n, 2)

    fig, ax = plt.subplots()
    fig.suptitle("spring", fontsize=14)
    ax.plot(r_a, r_b)
    ax.set_title("x")
    ax.set_xlim(-2, 2)

    plt.show()
