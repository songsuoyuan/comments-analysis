#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

from collections import Counter

f = open('new_feature_opinion.txt', 'r')
feature_opinion = []
feature = []
opinion = []
fo = []
empty = 0
imfeature = 0
imopinion = 0

for i in range(103):
    s = f.readline().decode('utf-8')[:-1]
    p = yaml.load(s)
    feature_opinion.append(p)
    if len(p) == 0:
        empty += 1
        continue
    else:
        for each in p:
            fopair = []
            if each[0][0] == 'h':
                imfeature += 1
                feature.append(each[0][1:])
                fopair.append(each[0][1:])
            else:
                feature.append(each[0])
                fopair.append(each[0])
            if each[1][0] == 'h':
                imopinion += 1
                opinion.append(each[1][1:])
                fopair.append(each[1][1:])
            else:
                opinion.append(each[1])
                fopair.append(each[1])
            fo.append(tuple(fopair))

F = Counter(feature)
print len(F), len(feature), imfeature
#for t in F.most_common(len(F)):
#    print t[0], t[1]

O = Counter(opinion)
print len(O), len(opinion), imopinion
#for r in O.most_common(len(O)):
#    print r[0], r[1]

FO = Counter(fo)
print len(FO)

for i in FO.most_common(len(FO)):
    print i[0][0], i[0][1], i[1]



print empty, len(fo)