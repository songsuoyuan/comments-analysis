#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')
sentence = []

g = open('index.txt', 'r')    
f = open('raw_comment.txt', 'r')
for i in range(141546):
    sentence.append(f.readline().decode('utf-8')[:-1])

for i in range(199):
    line = g.readline().decode('utf-8')[:-1]
    r = re.search('[\d]+', line)
    if line[r.end()+1:] != sentence[int(r.group())]:
        print i

