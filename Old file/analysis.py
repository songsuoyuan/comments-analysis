#!/usr/bin/env python
# -*- coding: utf-8 -*-

rate = []
f = open('rate.txt','r')
for line in f.readlines():
    rate.append(map(float, line.split(',')))

import 