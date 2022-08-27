from math import sqrt


def spring(start, end, coils, width, init_len=0.5):
    r_start = start
    r_end = end
    n = coils
    r_s = []
    length = sqrt((r_end[0] - r_start[0]) ** 2 + (r_end[1] - r_start[1]) ** 2)
    u_t = [(r_end[0] - r_start[0]) / length, (r_end[1] - r_start[1]) / length]
    u_n = [(0 * u_t[0] + (-1) * u_t[1]), 1 * u_t[0] + 0 * u_t[1]]
    w = width

    r1 = [start[0], start[0]+u_t[0]*init_len]
    r2 = [start[1], start[1]+u_t[1]*init_len]
    length = length-(2*init_len)
    for i in range(1, n + 1):
        r_x = r1[1] + length / (2 * n) * (2 * i - 1) * u_t[0] + 0.5 * sqrt(w ** 2 - (length ** 2 / n ** 2)) * (
            -1) ** i * u_n[0]
        r_y = r2[1] + length / (2 * n) * (2 * i - 1) * u_t[1] + 0.5 * sqrt(w ** 2 - (length ** 2 / n ** 2)) * (
            -1) ** i * u_n[1]
        r_i = [r_x, r_y]
        r_s.append(r_i)

    for r in r_s:
        r1.append(r[0])
        r2.append(r[1])

    r1.append(r_end[0] - u_t[0]*init_len)
    r1.append(r_end[0])

    r2.append(r_end[1] - u_t[1]*init_len)
    r2.append(r_end[1])
    return r1, r2
