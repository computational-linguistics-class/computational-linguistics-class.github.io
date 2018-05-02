'''
eval.py

Score predicted rankings using Average Precision

USAGE: 
python eval.py <conditionPOS> <conditionNEG> <rankingfile>
'''

import os, sys
import csv

def read_rankfile(fname):
    subjects = []
    with open(fname, 'rU') as fin:
        for line in fin:
            subjects.append(line.strip())
    return subjects

def read_gold():
    metafile = '../data/anonymized_user_info_by_chunk.csv'
    conditions = {}
    with open(metafile, 'rU') as fin:
        rdr = csv.DictReader(fin)
        for row in rdr:
            person = row['anonymized_screen_name']
            cond = row['condition']
            if cond not in ['ptsd','control','depression']:
                continue
            conditions[person] = cond
    return conditions

def clean_rankings(ranks, gold, condPOS, condNEG):
    '''
    Remove from ranks any people whose true condition is not
    either condPOS or condNEG
    '''
    return [p for p in ranks if gold[p] in [condPOS, condNEG]]

def average_precision(rankedpeople, goldconditions, condPOS, condNEG):
    '''
    Compute the average precision for a ranked list of people, 
    where their true conditions are given in goldconditions.
    :param rankedpeople: list of strings
    :param goldconditions: dict of {string: string} mapping people to conditions
    :param condPOS: string; condition to use as positive class
    :param condNEG: string; condition to use as negative class
    '''
    ap = 0.0
    
    ## Solution start
    def prec(l):
        return float(sum(l))/len(l)
    
    goldranks = [1. if goldconditions[p]==condPOS else 0 for p in rankedpeople]
    n = sum(goldranks)
    total = 0.0
    for i, p in enumerate(goldranks):
        if p==1:
            total += prec(goldranks[:i+1])
    ap = total / n
    ## Solution end
    
    return ap

if __name__=="__main__":
   condPOS = sys.argv[1]
   condNEG = sys.argv[2]
   rankingfile = sys.argv[3]
   
   predrankings = read_rankfile(rankingfile)
   gold_conditions = read_gold()
   final_rankings = clean_rankings(predrankings, gold_conditions, condPOS, condNEG)
   
   ap = average_precision(final_rankings, gold_conditions, condPOS, condNEG)
   
   print('Average precision: %0.4f\n' % (ap))
