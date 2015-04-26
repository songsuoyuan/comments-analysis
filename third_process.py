#!/usr/bin/env python
# -*- coding: utf-8 -*-


# [Finished in 9719.5s]
# utf-8 setting
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')
# dumping and loading data
import pickle

# regular expression
import re

# POS package
import jieba
jieba.load_userdict('user_dict.txt')
import jieba.posseg as posseg

from_file = open('mutual_matrix.pkl','rb')
(nouns_dict, adjcs_dict, mutual_matrix) = pickle.load(from_file)

# nouns_dict: (0: u'手机')
# adjcs_dict: (0: u'不错')
# create inverse dict
inv_nouns_dict = dict(zip(nouns_dict.values(), nouns_dict.keys()))
inv_adjcs_dict = dict(zip(adjcs_dict.values(), adjcs_dict.keys()))
# inv_nouns_dict[u'东西'] = 1
# inv_adjcs_dict[u'好'] = 1

# left adjcs:
left_adjcs = {}
# left nouns:
left_nouns = {}

f = open('comment.txt', 'r')

def distance(line, w1, w2):
    # w1: noun, w2: adjc
    dist = 100
    punctuation = [u'\u3002',u'\uff1f',u'\uff01',u'\uff0c',
         u'\u3001',u'\uff1b',u'\uff1a',u'\uff08',u'\uff09',
         u'\uff5e','.','?','!',',',';',':','(',')','~',' ']
    w1_location = []
    w2_location = []
    for each in re.finditer(w1, line):
        w1_location.append((each.start(), each.end()))
    for each in re.finditer(w2, line):
        w2_location.append((each.start(), each.end()))
    for p1 in w1_location:
        for p2 in w2_location:
            # two cases
            if p1[1] <= p2[0]:
                pun_count = 0
                for i in range(p1[1], p2[0]):
                    if line[i] in punctuation:
                        pun_count += 1
                if 5 * pun_count + 1.0 * (p2[0] - p1[1]) < dist:
                    dist = 5 * pun_count + (p2[0] - p1[1])
            elif p2[1] <= p1[0]:
                pun_count = 0
                for i in range(p2[1], p1[0]):
                    if line[i] in punctuation:
                        pun_count += 1
                if 5 * pun_count + 1.5 * (p1[0] - p2[1]) < dist:
                    dist = 5 * pun_count + 1.5 * (p1[0] - p2[1])
    return dist 

# 141546
for i in range(141546):
    line = f.readline().decode('utf-8')[:-1]
    nouns = []
    adjcs = []
    words = posseg.cut(line)
    for w in words:
        if w.flag[0] == 'n':
            nouns.append(w.word)
        if w.flag[0] == 'a':
            adjcs.append(w.word)
    for n in nouns:
        for a in adjcs:
            if inv_nouns_dict.has_key(n) and inv_adjcs_dict.has_key(a):
                n_indx = inv_nouns_dict[n]
                a_indx = inv_adjcs_dict[a]
                d = distance(line, n, a)
                m = mutual_matrix[n_indx][a_indx]
                # print i, n, a, distance(line, n, a), mutual_matrix[n_indx][a_indx]


    


