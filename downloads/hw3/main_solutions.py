import os
import csv
import subprocess
import re
import random
import numpy as np


def read_in_shakespeare():
  '''Reads in the Shakespeare dataset processesit into a list of tuples.
     Also reads in the vocab and play name lists from files.

  Each tuple consists of
  tuple[0]: The name of the play
  tuple[1] A line from the play as a list of tokenized words.

  Returns:
    tuples: A list of tuples in the above format.
    document_names: A list of the plays present in the corpus.
    vocab: A list of all tokens in the vocabulary.
  '''

  tuples = []

  with open('will_play_text.csv') as f:
    csv_reader = csv.reader(f, delimiter=';')
    for row in csv_reader:
      play_name = row[1]
      line = row[5]
      line_tokens = re.sub(r'[^a-zA-Z0-9\s]', ' ', line).split()
      line_tokens = [token.lower() for token in line_tokens]

      tuples.append((play_name, line_tokens))

  with open('vocab.txt') as f:
    vocab =  [line.strip() for line in f]

  with open('play_names.txt') as f:
    document_names =  [line.strip() for line in f]

  return tuples, document_names, vocab

def get_row_vector(matrix, row_id):
  return matrix[row_id, :]

def get_column_vector(matrix, col_id):
  return matrix[:, col_id]

def create_term_document_matrix(line_tuples, document_names, vocab):
  '''Returns a numpy array containing the term document matrix for the input lines.

  Inputs:
    line_tuples: A list of tuples, containing the name of the document and 
    a tokenized line from that document.
    document_names: A list of the document names
    vocab: A list of the tokens in the vocabulary

  Let n = len(document_names) and m = len(vocab).

  Returns:
    td_matrix: A mxn numpy array where the number of rows is the number of documents
        and each column corresponds to a token in the corpus. A_ij contains the
        frequency with which word i occurs in document j.
    vocab: A list containing the tokens being represented by each column.
  '''

  vocab_to_id = dict(zip(vocab, range(0, len(vocab))))
  docname_to_id = dict(zip(document_names, range(0, len(vocab))))

  # BEGIN SOLUTION
  matrix = np.zeros([len(vocab), len(document_names)])

  for document, tokens in line_tuples:
    column_id = docname_to_id.get(document, None)
    if column_id is None:
        continue
    for word in tokens:
      row_id = vocab_to_id.get(word, None)
      if row_id is None:
          continue
      matrix[row_id, column_id] += 1

  return matrix
  # END SOLUTION

def create_term_context_matrix(line_tuples, vocab, context_window_size=1):
  '''Returns a numpy array containing the term context matrix for the input lines.

  Inputs:
    line_tuples: A list of tuples, containing the name of the document and 
    a tokenized line from that document.
    vocab: A list of the tokens in the vocabulary

  Let n = len(vocab).

  Returns:
    tc_matrix: A nxn numpy array where A_ij contains the frequency with which
        word j was found within context_window_size to the left or right of
        word i in any sentence in the tuples.
    vocab: A list containing the tokens being represented by each column.
  '''

  vocab_to_id = dict(zip(vocab, range(0, len(vocab))))

  # BEGIN SOLUTION
  matrix = np.zeros([len(vocab), len(vocab)])

  for document, tokens in line_tuples:
    for idx in range(len(tokens)):
      for wdx in range(1, context_window_size+1):
        prev_word = tokens[idx - wdx] if idx-wdx >= 0 else None
        next_word = tokens[idx + wdx] if idx+wdx < len(tokens) else None
        
        row_id = vocab_to_id.get(tokens[idx], None)
        if row_id is None:
            continue
        
        if prev_word is not None:
          column_id = vocab_to_id.get(prev_word, None)
          if column_id is None:
              pass
          else:
              matrix[row_id, column_id] += 1
        if next_word is not None:
          column_id = vocab_to_id.get(next_word, None)
          if column_id is None:
              pass
          else:
              matrix[row_id, column_id] += 1

  return matrix
  # END SOLUTION

def create_PPMI_matrix(term_context_matrix):
  '''Given a term context matrix, output a PPMI matrix.
  
  See section 15.1 in the textbook.
  
  Hint: Use numpy matrix and vector operations to speed up implementation.
  
  Input:
    term_context_matrix: A nxn numpy array, where n is
        the numer of tokens in the vocab.
  
  Returns: A nxn numpy matrix, where A_ij is equal to the
     point-wise mutual information between the ith word
     and the jth word in the term_context_matrix.
  '''       
  
  # BEGIN SOLUTION
  n = term_context_matrix.shape[0]
  e = 1e-6
  PPMI_matrix = np.zeros([n, n])
  denominator = np.sum(term_context_matrix+e)
  
  p_ab = (term_context_matrix + e) / denominator
  
  p_a = np.sum(p_ab, axis=1)[:,None]  # sum each row
  p_b = np.sum(p_ab, axis=0)[None,:]  # sum each col
  
  denom_mat = np.ones(term_context_matrix.shape)
  denom_mat /= p_a
  denom_mat /= p_b
  
  pmi_mat = np.log2(p_ab * denom_mat)
  ppmi_mat = np.maximum(pmi_mat, 0.)
  return ppmi_mat
  
  # END SOLUTION

def create_tf_idf_matrix(term_document_matrix):
  '''Given the term document matrix, output a tf-idf weighted version.

  See section 15.2.1 in the textbook.
  
  Hint: Use numpy matrix and vector operations to speed up implementation.

  Input:
    term_document_matrix: Numpy array where each column represents a document 
    and each row, the frequency of a word in that document.

  Returns:
    A numpy array with the same dimension as term_document_matrix, where
    A_ij is weighted by the inverse document frequency of document h.
  '''

  # BEGIN SOLUTION
  n = float(term_document_matrix.shape[1]) # Number of documents
  num_docs_with = np.sum(term_document_matrix > 0, axis=1)
  idf = np.log(n / num_docs_with)
  return np.multiply(term_document_matrix, idf[:,np.newaxis]) 
  
  # Alt solution:
  # term_in_doc = np.minimum(term_document_matrix, 1.)  # entry=1 if term is in doc, 0 otherwise
  # df_vec = np.sum(term_in_doc, axis=1.)[:,None] # sum each row
  # idf_vec = 1. / df_vec
  # tf_idf = term_document_matrix * idf_vec
  # return tf_idf
  # END SOLUTION

def compute_cosine_similarity(vector1, vector2):
  '''Computes the cosine similarity of the two input vectors.

  Inputs:
    vector1: A nx1 numpy array
    vector2: A nx1 numpy array

  Returns:
    A scalar similarity value.
  '''
  
  # BEGIN SOLUTION
  num = np.dot(vector1, vector2)
  den1 = np.sqrt((vector1**2).sum())
  den2 = np.sqrt((vector2**2).sum())
  return num / (den1 * den2)
  # END SOLUTION

def compute_jaccard_similarity(vector1, vector2):
  '''Computes the cosine similarity of the two input vectors.

  Inputs:
    vector1: A nx1 numpy array
    vector2: A nx1 numpy array

  Returns:
    A scalar similarity value.
  '''
  
  # BEGIN SOLUTION
  num = np.minimum(vector1, vector2).sum()
  den = np.maximum(vector1, vector2).sum()
  return num / den
  # END SOLUTION

def compute_dice_similarity(vector1, vector2):
  '''Computes the cosine similarity of the two input vectors.

  Inputs:
    vector1: A nx1 numpy array
    vector2: A nx1 numpy array

  Returns:
    A scalar similarity value.
  '''

  # BEGIN SOLUTION
  num = 2. * np.minimum(vector1, vector2).sum()
  den = (vector1 + vector2).sum()
  return num / den
  # END SOLUTION

def rank_plays(target_play_index, term_document_matrix, similarity_fn):
  ''' Ranks the similarity of all of the plays to the target play.

  Inputs:
    document_names: List of document names, corresponding to  
      term_document_matrix columns (i.e. name of document corresponding to 
      term_document_matrix[:,i] is given by document_names[i])
    target_play_index: The integer index of the play we want to compare all others against.
    term_document_matrix: The term-document matrix as a mxn numpy array.
    similarity_fn: Function that should be used to compared vectors for two
      documents. Either compute_dice_similarity, compute_jaccard_similarity, or
      compute_cosine_similarity.

  Returns:
    A length-n list of strings corresponding to play names,
    ordered by decreasing similarity to the play indexed by target_play_index
  '''
  
  # BEGIN SOLUTION
  m, n = term_document_matrix.shape
  sims = np.zeros(n)
  v_tgt = get_column_vector(term_document_matrix, target_play_index)
  for i in range(n):
    v_doc = get_column_vector(term_document_matrix, i)
    sims[i] = similarity_fn(v_tgt, v_doc)
  sims_sort = np.argsort(-sims)
  return sims_sort
  # END SOLUTION

def rank_words(target_word_index, matrix, similarity_fn):
  ''' Ranks the similarity of all of the words to the target word.

  Inputs:
    vocab: List of terms, corresponding to target_word_index rows (i.e. word corresponding
      to target_word_index[i,:] is given by vocab[i])
    target_word_index: The index of the word we want to compare all others against.
    matrix: Numpy matrix where the ith row represents a vector embedding of the ith word.
    similarity_fn: Function that should be used to compared vectors for two word
      ebeddings. Either compute_dice_similarity, compute_jaccard_similarity, or
      compute_cosine_similarity.

  Returns:
    A length-n list of words, ordered by decreasing similarity to the 
    target word indexed by word_index
  '''

  # BEGIN SOLUTION
  n, __ = matrix.shape
  sims = np.zeros(n)
  v_tgt = get_row_vector(matrix, target_word_index)
  for i in range(n):
    v_wrd = get_row_vector(matrix, i)
    sims[i] = similarity_fn(v_tgt, v_wrd)
  sims_sort = np.argsort(-sims)
  return sims_sort
  # END SOLUTION

if __name__ == '__main__':
  tuples, document_names, vocab = read_in_shakespeare()

  print('Computing term document matrix...')
  td_matrix = create_term_document_matrix(tuples, document_names, vocab)

  print('Computing tf-idf matrix...')
  tf_idf_matrix = create_tf_idf_matrix(td_matrix)

  print('Computing term context matrix...')
  tc_matrix = create_term_context_matrix(tuples, vocab, context_window_size=2)

  print('Computing PPMI matrix...')
  PPMI_matrix = create_PPMI_matrix(tc_matrix)

  random_idx = random.randint(0, len(document_names)-1)
  similarity_fns = [compute_cosine_similarity, compute_jaccard_similarity, compute_dice_similarity]
  for sim_fn in similarity_fns:
    print('\nThe 10 most similar plays to "%s" using %s are:' % (document_names[random_idx], sim_fn.__qualname__))
    ranks = rank_plays(random_idx, td_matrix, sim_fn)
    for idx in range(0, 10):
      doc_id = ranks[idx]
      print('%d: %s' % (idx+1, document_names[doc_id]))

  word = 'juliet'
  vocab_to_index = dict(zip(vocab, range(0, len(vocab))))
  for sim_fn in similarity_fns:
    print('\nThe 10 most similar words to "%s" using %s on term-context frequency matrix are:' % (word, sim_fn.__qualname__))
    ranks = rank_words(vocab_to_index[word], tc_matrix, sim_fn)
    for idx in range(0, 10):
      word_id = ranks[idx]
      print('%d: %s' % (idx+1, vocab[word_id]))

  word = 'juliet'
  vocab_to_index = dict(zip(vocab, range(0, len(vocab))))
  for sim_fn in similarity_fns:
    print('\nThe 10 most similar words to "%s" using %s on PPMI matrix are:' % (word, sim_fn.__qualname__))
    ranks = rank_words(vocab_to_index[word], PPMI_matrix, sim_fn)
    for idx in range(0, 10):
      word_id = ranks[idx]
      print('%d: %s' % (idx+1, vocab[word_id]))
