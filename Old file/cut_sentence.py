#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from collections import Counter

import re
import jieba
jieba.load_userdict("user_dict.txt")
import jieba.posseg as pseg
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

cutlist = ("。？！，、；：“”‘’（）【】《》～…—ˇ"
           ".?!,;:()~-| ").decode('utf-8')

# f = open('comment.txt','r')
f = open('comment.txt','r')
# g = open('noun.txt','w')
# h = open('adjs.txt','w')

lenlist  = []
count_dict = {}

for i in range(200):
    line = f.readline().decode('utf-8')[:-1]
    for sent in re.split(u'[\s\u3002\uff1f\uff01\uff0c\u3001\uff1b\uff1a\u201c\u201d\u2018\u2019\uff08\uff09\u3010\u3011\u300a\u300b\uff5e.?!,;:()~-]', line):
        if sent:
            words = pseg.cut(sent)
            noun = []
            adjs = []
            seq = 0 
            for w in words:
                seq += 1
                if w.flag[0] == 'n':
                    noun.append((w.word, seq))
                    continue
                if w.flag[0] == 'a':
                    adjs.append((w.word, seq))
                    continue
            if len(noun) > 0 and len(adjs) > 0:
                for n in noun:
                    for a in adjs:
                        print i+1, n[0], a[0], a[1]-n[1]

