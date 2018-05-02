#!/usr/bin/env python

'''
util.py

Utility functions for reading and writing data.

'''

import csv
import os, sys
import tarfile
import json
import pickle as pkl

BASEDIR = '..'


###################################################
# Functions for loading and extracting data
###################################################

def get_tweets_element(bytestr, elem='text'):
    tweets = bytestr.splitlines()
    tweetdata = []
    for t in tweets:
        tweet = json.loads(t)
        tweetdata.append(tweet[elem])
    return tweetdata

def get_tweets(datadir, ci, subj=None):
    '''
    Get tweet data for specified users, located in datadir
    under chunk index range denoted by ci
    
    :returns: a dict indexed by subject ID, where the values
      are byte strings of the tweets in json format
    '''
    contentDict = {}
    ci_low, ci_hi = ci
    for chunkIndex in range(ci_low, ci_hi+1):
        dataloc = os.path.join(datadir, "%d.tgz" % chunkIndex)
        tar = tarfile.open(dataloc, "r:gz")
        for member in tar.getmembers(): #each member = subject
            f = tar.extractfile(member)
            content = f.read() #.splitlines()
            subjID = (member.name).split('.')[0]
            if subj is not None:
                if subjID not in subj:
                    continue
            contentDict[subjID] = content
        tar.close()
        
    return contentDict


def get_subj_data(datafile, target_condition=None):
    '''
    Get subject data from CLPsych meta data file
    
    NB: The chunk_index in the meta data file does not correspond
    to the chunks in the final train/test directories...ignore it.
    '''
    subjects = {}
    with open(datafile, 'r') as fin:
        rdr = csv.DictReader(fin)
        for row in rdr:
            if target_condition is not None:
                if row['condition'] != target_condition:
                    continue
            subjects[row['anonymized_screen_name']] =  {k: row[k] for k in ['age', 'num_tweets', 'gender', 'condition']}
    return subjects


def load_data(split):
    '''
    Loads CLPsych shared task data.
    
    :param split: str (one of 'train', 'dev', or 'test')
    :returns: list of (userID, userData, userTweets) tuples
    '''
    if split=='train':
        dname = os.path.join(BASEDIR, 'data/final_training_data')
        ci = (0, 49)
    elif split=='dev':
        dname = os.path.join(BASEDIR, 'data/final_testing_data')
        ci = (60, 65)
    elif split=='test':
        dname = os.path.join(BASEDIR, 'data/final_testing_data')
        ci = (66, 89)
    else:
        sys.stderr.write('Invalid split passed; must be one of "train", "dev", or "test"\n')
        return []
    sys.stderr.write('Loading %s data...' % split)
    metafile = os.path.join(BASEDIR, 'data/anonymized_user_info_by_chunk.csv')
    subjects = get_subj_data(metafile)
    subj_tweet_data = get_tweets(dname, ci)
    sys.stderr.write('done\n')
    
    finaldata = [(k, subjects[k], subj_tweet_data[k]) for k in subj_tweet_data]
    
    return finaldata

###################################################
# Functions for loading and saving language models
###################################################

def write_lm(lm, dest):
    with open(dest, 'wb') as fout:
        pkl.dump(lm, fout)

def load_lm(src):
    with open(src, 'rb') as fin:
        lm = pkl.load(fin)
    order = len(list(lm.keys())[0])
    return lm, order
    