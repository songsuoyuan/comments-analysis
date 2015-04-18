#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')
from collections import Counter
#-------------------------------------
#匹配全部标点符号 
#bug: 不能读取最后一行, fixed at Jan 27.
#bug: 不能匹配 '，。！、...', fixed at Jan 27.
 
# f = open('short_comment.txt','r')
# g = open('short_comment.txt.tmp','w')
# 
# for i in range(103):
#     s = f.readline()[:-1].decode('utf-8')
#     p = re.compile(r'[\.\?!,;:\"()\[\]~| ]+')
#     z = re.compile(u'[\u3002\uff1f\uff01\uff0c\u3001'
#                    u'\uff1b\uff1a\u201c\u201d\u2018'
#                    u'\u2019\uff08\uff09\u3010\u3011'
#                    u'\u300a\u300b]+')
#     r  = re.match(p, s)
#     rz = re.match(z, s)
#     if r and r.group() == s:
#         print i+1, r.group()
#         g.write('\n')
#         continue
#     elif rz and rz.group() == s:
#         print i+1, rz.group()
#         g.write('\n')
#         continue
#     else:
#         g.write(s+'\n')
# f.close()
# g.close()
# 
##--------------------------------------

# #--------------------------------------
# #匹配多重符号
# 
# f = open('comment.txt','r')
# g = open('comment.txt.tmp','w')
# for i in range(141546):
#     s = f.readline()[:-1].decode('utf-8')
#     p = re.compile(u'[\u3002\uff1f\uff01\uff0c\u3001'
#                u'\uff1b\uff1a\u201c\u201d\u2018'
#                u'\u2019\uff08\uff09\u3010\u3011'
#                u'\u300a\u300b\uff5e\u2026\u2014'
#                u'\u02c7'
#                u'.?!,;:()~-]{2,}')
#     gs = ''
#     start = 0
#     for m in re.finditer(p, s):
#         print i + 1, s[m.start():m.end()]
#         gs += s[start:m.start()]
#         gs += s[m.start()]
#         start = m.end()
#     gs += s[start:]
#     g.write(gs + '\n')
# 
# f.close()
# g.close()
# # ------------------------------------

# #--------------------------------------
# #匹配纯数字, 纯英文
# f = open('short_comment.txt','r')
# g = open('comment.txt.tmp','w')
# for i in range(141546):
#     s = f.readline()[:-1].decode('utf-8')
#     r = re.match(r'[\d]+', s)
#     if r and r.group() == s:
#         print i+1, s
#         g.write('\n')
#         continue
#     rz = re.match(r'[a-zA-Z]+', s)
#     if rz and rz.group() == s:
#         print i+1, s
#         g.write('\n')
#         continue    
#     g.write(s+'\n')
# 
# f.close()
# g.close()
# # --------------------------------------

# --------------------------------------
# 匹配重复评论
# f = open('short_comment.txt','r')
# g = open('comment.txt.tmp','w')

# def check_duplicate(s, k):
#     l = len(s)
#     for i in range(2, k+1):
#         if s[:l/k] != s[(i-1)*l/k:i*l/k]:
#             return False
#     return True
# 
# for i in range(103):
#     s = f.readline()[:-1].decode('utf-8')
#     l = len(s)
#     p = range(100,1,-1)
#     flag = False
#     for k in p:
#         if (l > 0 and l % k == 0 and check_duplicate(s, k)):
#             print i+1, k, s
#             flag = True
#             break
#     # if flag:
#     #     print i+1, s
#         # g.write(s[:l/k]+'\n')
#     # else:
#         # g.write(s+'\n')

# f.close()
# g.close()

