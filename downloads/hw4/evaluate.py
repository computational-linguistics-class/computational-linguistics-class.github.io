'''

evaluate.py

Evaluate a predicted clustering against a ground-truth clustering
using paired-F score

Usage: 
  python evaluate.py <GROUND-TRUTH-FILE> <PREDICTED-CLUSTERS-FILE>
'''

import os, sys
import numpy as np
import itertools
import argparse

def read_clusters(fname):
    clus = {}
    with open(fname, 'rU') as fin:
        for line in fin:
            tgt, __, cluswords = line.strip().split(' :: ')
            if tgt not in clus:
                clus[tgt] = []
            clus[tgt].append(cluswords.strip().split())
    return clus

def eval_clustering(gc, pc):
    N = len(gc)
    gold_pairs = set()
    for gclus in gc:
        for pair in itertools.combinations(gclus, 2):
            gold_pairs.add(tuple(sorted(pair)))
    pred_pairs = set()
    for pclus in pc:
        for pair in itertools.combinations(pclus, 2):
            pred_pairs.add(tuple(sorted(pair)))
    ovlp = gold_pairs & pred_pairs
    
    try:
        precision = float(len(ovlp)) / len(pred_pairs)
    except ZeroDivisionError:
        precision = 1.
    
    try:
        recall = float(len(ovlp)) / len(gold_pairs)
    except ZeroDivisionError:
        recall = 1.
    
    try:
        f = 2 * precision * recall / (precision + recall)
    except ZeroDivisionError:
        f = 0.
    return f, N


def eval_file(gf, pf):
    
    gold_clus = read_clusters(gf)
    pred_clus = read_clusters(pf)
    
    targets = set(gold_clus.keys()) & set(pred_clus.keys())
    
    if len(targets)==0:
        sys.stderr.write('No overlapping target words in ground-truth and predicted files\n')
        return None
    
    fs = []
    ns = []
    print("TGT\t\tN\t\tF-SCORE")
    for tgt in targets:
        clus_f, n_gs_clus = eval_clustering(gold_clus[tgt], pred_clus[tgt])
        fs.append(clus_f)
        ns.append(n_gs_clus)
        print('\t\t'.join((tgt, '%d' % n_gs_clus, '%0.4f' % clus_f)))
    
    fs = np.array(fs)
    ns = np.array(ns)
    avg_f = np.average(fs, weights=ns)
    print("====================")
    print("Average Paired F-Score:  %0.4f" % avg_f)

if __name__=="__main__":
    
    goldfile = sys.argv[1]
    predfile = sys.argv[2]
    
    if not os.path.isfile(goldfile):
        sys.stderr.write('Invalid ground truth filename\n')
        exit(0)
    if not os.path.isfile(predfile):
        sys.stderr.write('Invalid predicted clusters filename\n')
        exit(0)
    
    eval_file(goldfile, predfile)
