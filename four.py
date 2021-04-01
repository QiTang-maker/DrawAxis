# coding=gbk

"""
Author：代英杰
Date：2021年03月29日 10:30
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist.axislines import Subplot
from scipy import interpolate


def sommth_plot(x_arr, y_arr):
    fig = plt.figure()  # 创建一个figure
    ax = Subplot(fig, 111)  # 利用Subplot将figure加入ax
    fig.add_axes(ax)
    ax.axis['bottom'].set_axisline_style("->", size = 1.5)  # x轴加上箭头
    ax.axis['left'].set_axisline_style("->", size = 1.5)  # y轴加上上箭头
    ax.axis['top'].set_visible(False)  # 去除上方坐标轴
    ax.axis['right'].set_visible(False)  # 去除右边坐标轴
    xmin = min(x_arr)
    xmax = max(x_arr)
    xnew = np.arange(xmin, xmax, 0.0005)  # 在最大最小值间以间隔为0.0005插入点
    func = interpolate.interp1d(x_arr, y_arr)
    ynew = func(xnew)  # 得到插入x对应的y值
    plt.plot(xnew, ynew, '-')  # 绘制图像
    plt.show()  # show图像
    plt.savefig("D:\\课程\\大三下\\智能系统优化设计\\4.png")
    plt.close()
    pass


def assignment(x_arr, y_arr):
    for temp in range(0, 65000):
        x_num = temp * 0.001
        y_num = 100 - 1.35 * x_num
        x_arr.append(x_num)
        y_arr.append(y_num)
        if y_num <= 20:
            break

    x_split = x_num

    for temp in range(int(x_split * 1000), 65000):
        x_num = temp * 0.001
        y_num = 20 + 0.09 * (x_num - x_split) ** 2 - 4.36 * (x_num - x_split)
        x_arr.append(x_num)
        y_arr.append(y_num)
        if y_num <= 0:
            break
    pass


def main():
    x = []
    y = []
    assignment(x, y)
    sommth_plot(x, y)
    pass


if __name__ == '__main__':
    main()
