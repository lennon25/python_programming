#!/usr/bin/env python3

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建randomwalk实例，并将其包含的点绘制出来

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.show()

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

