#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------
# forth process -- count word freq
#
# dump count_dict to dict.pkl
#
# for reference: [Finished in 34.9s]
#
# PS: do not use jieba.enable_parallel, no help!
# -----------------------------------------------------------------

# utf-8 setting
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

# POS package
import jieba
jieba.load_userdict('user_dict.txt')
import jieba.posseg as posseg

# for dumping dict
import pickle

f = open('comment.txt', 'r')

count_dict = {}

for i in range(141546):
    line = f.readline().decode('utf-8')[:-1]
    words = posseg.cut(line, HMM=False)
    for w in words:
        if w.flag != 'x':
            if count_dict.has_key(w.word):
                count_dict[w.word] += 1
            else:
                count_dict[w.word]  = 1

to_file = open('dict.pkl','wb')
pickle.dump(count_dict, to_file)
