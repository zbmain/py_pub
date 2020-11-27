#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zb
# @Time    : 2020/11/17 23:21
# @Blog    : https://blog.zbmain.com

import platform
import os
sys_ = platform.system().lower()
__common_data_path = sys_ == 'linux' and '/home/common/' or sys_ == 'darwin' and '/Users/common/' or '/user/common/'
'''
    Mac Win|Linux运行环境下数据文件绝对路径地址
    [Mac|Win|Linux]
    - os.path.join(__common_data_path,file_path)
'''


def __join(filepath):
    '''
    绝对数据路径拼接

    :param filepath:
    :return: /common/ [filepath]
    '''
    return os.path.join(__common_data_path, filepath)


if __name__ == '__main__':
    print(__join('main.py'))
