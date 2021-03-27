#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zb
# @Time    : 2020/11/27 16:43
# @Blog    : https://blog.zbmain.com
import argparse

parser = argparse.ArgumentParser()
# ----set argument----
parser.add_argument("-t", "--train", action='store_true', default=False, help="Whether to run training.")
parser.add_argument("-n", "--num", default=0, type=int, help="num_Epoch or num_Iter")
# ----set end----
args = parser.parse_args()
