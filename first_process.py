#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------
# first process -- count (noun, adjs) pair
#
# dump pair_dict to pair_dict.txt
#
# for reference: [Finished in 343.7s]
# -----------------------------------------------------------------

# utf-8 setting
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

# POS package
import jieba
jieba.load_userdict('user_dict.txt')
import jieba.posseg as posseg

# regular expression
import re

# for dumping dict
import pickle

f = open('comment.txt', 'r')

pair_dict = {}

# 141546
for i in range(141546):
    line = f.readline().decode('utf-8')[:-1]
    lseg = re.split((u'[\s\u3002\uff1f\uff01\uff0c\u3001\uff1b'
                     u'\uff1a\uff08\uff09\uff5e.?!,;:()~]'), line)
    for seg in lseg:
        words = posseg.cut(seg, HMM=False)
        nouns = []
        adjcs = []
        for w in words:
            if   w.flag[0] == 'n':
                nouns.append(w.word)
            elif w.flag[0] == 'a':
                adjcs.append(w.word)
        if len(nouns) > 0 and len(adjcs) > 0:
            for pair in [(x, y) for x in nouns for y in adjcs]:
                if pair_dict.has_key(pair):
                    pair_dict[pair] = (pair_dict[pair] 
                        + 1. / len(nouns) / len(adjcs))
                else:
                    pair_dict[pair] = 1. / len(nouns) / len(adjcs)

to_file = open('pair_dict.pkl','wb')
pickle.dump(pair_dict, to_file)