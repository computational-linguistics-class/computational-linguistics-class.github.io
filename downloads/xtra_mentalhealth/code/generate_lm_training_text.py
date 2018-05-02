'''
generate_lm_training_text.py

Generate training text for each condition of subject from the
training dataset. This text can be used to train language
models specific to each condition.
'''

import os
import util
import codecs

text = {'depression': [],
        'control': [],
        'ptsd': [] }

train = util.load_data('train')

for sid, sdata, tweets in train:
    cndn = sdata['condition']
    twts = util.get_tweets_element(tweets, 'text')
    twts = [codecs.encode(t, errors='ignore') for t in twts]
    try:
        text[cndn].extend(twts)
    except KeyError:  # some subjects have nothing listed here
        continue  

try:
    os.makedirs('../data/lm-training-text')
except FileExistsError:
    pass

for cndn, txtlist in text.items():
    with open(os.path.join('../data/lm-training-text', '%s_text.txt' % cndn), 'w') as fout:
        for txt in txtlist:
            fout.write(codecs.decode(txt)+'\n')
