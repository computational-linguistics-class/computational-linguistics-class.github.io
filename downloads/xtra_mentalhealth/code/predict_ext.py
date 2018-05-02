#!/usr/bin/env python

'''
predict_ext.py

Use this file to implement your extended model.

Usage:
python predict_lm.py <SPLIT> <CONDITION_POS_MODEL> <CONDITION_NEG_MODEL> <OUTFILE>

You may add or remove arguments as necessary; include a description in the README.
'''

from collections import *
import json
import os
import operator

import util


def score_subjects(data, lm_pos, lm_neg):
    '''
    Score the persons represented in data 
        
    :returns dict of {subjectID: score} where scores correspond to the likelihood that
             each subject has the positive condition as opposed to the negative condition
    '''
    
    # create a dict mapping subjectID to tweet text
    subj2tweets = {}
    for subjID, subjData, subjTweets in data:
        tweets = util.get_tweets_element(subjTweets, elem='text')
        subj2tweets[subjID] = tweets
    
    scores = {}
    ##### BEGIN SOLUTION #####
    
    # ( your model here )

    ##### END SOLUTION #####
    
    return scores



def write_rankings(user_scores, writeFile):
    sorted_dict = sorted(user_scores.items(), key=operator.itemgetter(1), reverse=True)
    with open(writeFile, 'w') as out:
        for user, score in sorted_dict:
            print(user)
            try:
                out.write(user + '\n')
            except:
                pass

if __name__ == '__main__':
    
    split = sys.argv[1]
    condPOSmodel = sys.argv[2]
    condNEGmodel = sys.argv[3]
    outfile = sys.argv[4]
    
    data = util.load_data(split)
    
    lm_pos, order_pos = util.load_lm(condPOSmodel)
    lm_neg, order_neg = util.load_lm(condNEGmodel)
    
    assert order_pos==order_neg
    
    subject_scores = score_subjects(data, lm_pos, lm_neg)
    
    write_rankings(subject_scores, outfile)
    
