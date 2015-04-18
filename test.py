#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jieba
jieba.enable_parallel(4)
jieba.load_userdict('user_dict.txt')
import jieba.posseg as posseg

# utf-8 setting
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

words = posseg.cut('东西好')
print dir(words)
for w in words:
    print w.word, w.flag

