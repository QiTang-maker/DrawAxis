# coding=gbk

"""
Author����Ӣ��
Date��2021��03��29�� 10:30
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist.axislines import Subplot
from scipy import interpolate


def sommth_plot(x_arr, y_arr):
    fig = plt.figure()  # ����һ��figure
    ax = Subplot(fig, 111)  # ����Subplot��figure����ax
    fig.add_axes(ax)
    ax.axis['bottom'].set_axisline_style("->", size = 1.5)  # x����ϼ�ͷ
    ax.axis['left'].set_axisline_style("->", size = 1.5)  # y������ϼ�ͷ
    ax.axis['top'].set_visible(False)  # ȥ���Ϸ�������
    ax.axis['right'].set_visible(False)  # ȥ���ұ�������
    xmin = min(x_arr)
    xmax = max(x_arr)
    xnew = np.arange(xmin, xmax, 0.0005)  # �������Сֵ���Լ��Ϊ0.0005�����
    func = interpolate.interp1d(x_arr, y_arr)
    ynew = func(xnew)  # �õ�����x��Ӧ��yֵ
    plt.plot(xnew, ynew, '-')  # ����ͼ��
    plt.show()  # showͼ��
    plt.savefig("D:\\�γ�\\������\\����ϵͳ�Ż����\\4.png")
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
