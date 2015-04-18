#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------
# second process -- construct mutual matrix
#
# dump (nouns_dict, adjcs_dict, mutual_matrix) to mutual_matrix.txt
#
# for reference: [Finished in 1.0s]
# -----------------------------------------------------------------

# utf-8 setting
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')
# for dumping 
import pickle
# math calculation
import math
# plot functions
import matplotlib.pyplot as plt

from_file = open('pair_dict.pkl','rb')
pair_dict = pickle.load(from_file)
sorted_pair_dict = sorted(pair_dict.items(), key=(lambda x: x[1]), 
                          reverse=True)

N = len(sorted_pair_dict)
freq = [item[1] for item in sorted_pair_dict]
log_freq = map(math.log10, 
    [item[1] for item in sorted_pair_dict if item[1] > pow(10,.5)])
N1 = len(log_freq)

# search top 50%, 80%, 90%, 95%
total_sum = sum(freq)
partl_sum = 0
quantile_pos = []
flags = [True] * 3

for i in range(N):
    partl_sum += freq[i]
    if flags[0] and partl_sum > 0.5 * total_sum:
        quantile_pos.append(i)
        flags[0] = False
    elif flags[1] and partl_sum > 0.7 * total_sum:
        quantile_pos.append(i)
        flags[1] = False
    elif flags[2] and partl_sum > 0.8 * total_sum:
        quantile_pos.append(i)
        flags[2] = False
    elif partl_sum > 0.9 * total_sum:
        quantile_pos.append(i)
        break

# quantile_pos = [67, 469, 1522, 5942]
# total_sum = 81642

def freq_item_plot(to_file_name):
    plt.plot(range(1,N1+1,1), log_freq, lw=2)
    plt.annotate('Total 80%, TF=4.21 ', 
                 xy=(1522, 0.62), xytext=(1480, 1.12),
                 arrowprops=dict(facecolor='black', 
                                 arrowstyle='-|>', 
                                 connectionstyle='arc'))
    plt.annotate('Total 70%, TF=15.9 ', 
                 xy=(469, 1.20), xytext=(440, 1.7),
                 arrowprops=dict(facecolor='black', 
                                 arrowstyle='-|>', 
                                 connectionstyle='arc'))
    plt.annotate('Total 50%, TF=146.8', 
                 xy=(67, 2.16), xytext=(40, 2.66),
                 arrowprops=dict(facecolor='black', 
                                 arrowstyle='-|>', 
                                 connectionstyle='arc'))
    plt.plot([1522,1522], [0,0.62], '--', color='black')
    plt.plot([469,  469], [0,1.20], '--', color='black')
    plt.plot([67,    67], [0,2.16], '--', color='black')
    plt.xticks([0, 67, 469, 1000, 1522, 2000],  
               ('0', '67', '469', '1000', '1522', '2000'))
    plt.title('Items -- log-frequency Plot')
    plt.xlabel('Items')
    plt.ylabel('Logarithm of frequency (base 10)')
    plt.savefig(to_file_name, bbox_inches='tight')
    plt.show()

prune_threshold = 15.94
prune_pair_dict = [it for it in sorted_pair_dict if it[1] > 15.94]
nouns = set([it[0][0] for it in prune_pair_dict])
adjcs = set([it[0][1] for it in prune_pair_dict])

# len(nouns) = 172, len(adjcs) = 80
nouns_len = len(nouns)
nouns_dict = dict(zip(range(nouns_len), list(nouns)))
adjcs_len = len(adjcs)
adjcs_dict = dict(zip(range(adjcs_len), list(adjcs)))

mutual_matrix = ([[0 for j in range(adjcs_len)] 
                 for i in range(nouns_len)])
for i in range(nouns_len):
    for j in range(adjcs_len):
        if pair_dict.has_key((nouns_dict[i], adjcs_dict[j])):
            v = pair_dict[(nouns_dict[i], adjcs_dict[j])]
            if v > prune_threshold:
                mutual_matrix[i][j] = v

to_file = open('mutual_matrix.pkl','wb')
pickle.dump((nouns_dict, adjcs_dict, mutual_matrix), to_file)

def log_mutual_matrix_plot(to_file_name):
    import numpy as np
    log_mutual_matrix = ([[0 for j in range(nouns_len)] 
                         for i in range(adjcs_len)])
    for i in range(nouns_len):
        for j in range(adjcs_len):
            if mutual_matrix[i][j] > 0:
                log_mutual_matrix[j][i] = (np.log10(
                                           mutual_matrix[i][j]))
    m = np.array(log_mutual_matrix)
    import pylab
    pylab.figure(figsize=(12,6))
    pylab.pcolor(m, cmap='spectral')
    pylab.colorbar()
    pylab.xlim([0, 172])
    pylab.title('Thermodynamic Plot')
    pylab.xlabel('Nouns')
    pylab.ylabel('Adjectives')
    pylab.savefig(to_file_name, bbox_inches='tight')
    pylab.show()