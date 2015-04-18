#!/usr/bin/env python
# -*- coding: utf-8 -*-

# utf-8 setting
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')
# dumping and loading data
import pickle

from_file = open('mutual_matrix.pkl','rb')
(nouns_dict, adjcs_dict, mutual_matrix) = pickle.load(from_file)

