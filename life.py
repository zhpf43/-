import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# 计算每个细胞的邻居数量
def count_neighbors(state):
    return (
        np.roll(state, -1, 0).astype(int)
        + np.roll(state, 1, 0).astype(int)
        + np.roll(state, -1, 1).astype(int)
        + np.roll(state, 1, 1).astype(int)
        + np.roll(np.roll(state, -1, 0), -1, 1).astype(int)
        + np.roll(np.roll(state, -1, 0), 1, 1).astype(int)
        + np.roll(np.roll(state, 1, 0), -1, 1).astype(int)
        + np.roll(np.roll(state, 1, 0), 1, 1).astype(int)
    )


# 随机初始状态
user_initial_state = np.random.choice([0, 1], size=(100, 100)).astype(int)


# 更新世界状态
def step(state):
    neighbors = count_neighbors(state)
    return (neighbors == 3) | ((state == 1) & (neighbors == 2))


# 运行游戏
def run_game(initial_state):
    state = initial_state
    fig, ax = plt.subplots()
    img = ax.imshow(state, cmap="binary")

    def animate(i):
        nonlocal state
        state = step(state)
        img.set_array(state)

    ani = animation.FuncAnimation(fig, animate, frames=100)
    plt.show()


def initialize(user_initial_state):
    num = eval(input("输入需要设置的点数:"))
    inp = np.zeros((2, num))
    for i in range(num):
        inp[1][i] = int(input("请输入第%d个横坐标:" % (i + 1)))
        inp[0][i] = int(input("请输入第%d个纵坐标:" % (i + 1)))
        user_initial_state[int(inp[0][i])][int(inp[1][i])] = 1
    return user_initial_state


# 随机初始状态
user_initial_state = np.random.choice([0, 1], size=(100, 100))

# user_initial_state = np.zeros((50, 50))

# initialize(user_initial_state)

run_game(user_initial_state)

# 歪比歪比阿巴阿巴
