import matplotlib.pyplot as plt
from physcis_systems.dynamic_spring import spring

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
