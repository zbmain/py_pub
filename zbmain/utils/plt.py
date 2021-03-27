#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zb
# @Time    : 2020/12/11 11:15
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

n = 0


def plt_epoch(arr, label='', color='red', locator_num=1, save_path='./tmp.png'):
    plt.figure(0)
    plt.plot(arr,label)
    plt.plot(arr,color=color,label=)


def show():
    '''释放'''
    plt.show()
