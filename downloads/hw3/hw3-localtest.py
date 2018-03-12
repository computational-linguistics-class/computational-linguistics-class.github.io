import random
import numpy as np

import main
import main_solutions


tuples, document_names, vocab = main_solutions.read_in_shakespeare()
N=6000


"""Check counts in term-document matrix"""
print('1.1')
soln_term_doc_matrix = main_solutions.create_term_document_matrix(tuples, document_names, vocab)
student_term_doc_matrix = main.create_term_document_matrix(tuples, document_names, vocab)
if len(student_term_doc_matrix) == 2:
    student_term_doc_matrix = student_term_doc_matrix[0]

i_lst = [random.randint(0, len(vocab)-1) for __ in range(3)]
j_lst = [random.randint(0, len(document_names)-1) for __ in range(3)]
for i, j in zip(i_lst, j_lst):
    try:
        stu_cnt = np.around(student_term_doc_matrix[i,j], 1)
    except Exception as e:
        print('Could not call create_term_document_matrix')
        stu_cnt = -1
    sol_cnt = np.around(soln_term_doc_matrix[i,j], 1)
    if stu_cnt != sol_cnt:
        print('Incorrect count for term document matrix row %d col %d: got %0.1f, should be %0.1f' % (i,j, stu_cnt, sol_cnt))
    else: print('Correct!')
        
"""Check counts in term-context matrix"""
print('1.2')
soln_term_ctx_matrix = main_solutions.create_term_context_matrix(tuples, vocab, context_window_size=2)
student_term_ctx_matrix = main.create_term_context_matrix(tuples, vocab, context_window_size=2)

if len(student_term_ctx_matrix)==2:
    student_term_ctx_matrix = student_term_ctx_matrix[0]

i = 1317 # the
j = 5124 # sword
sol_cnt = 49.
stu_cnt = np.around(student_term_ctx_matrix[i,j], 0)
if stu_cnt != sol_cnt:
    print('Incorrect count for term context matrix row %d col %d: got %0.1f, should be %0.1f' % (i,j, stu_cnt, sol_cnt))
else: print('Correct!')


"""Check values in tf-idf matrix"""
print('1.3')
soln_term_doc_matrix = main_solutions.create_term_document_matrix(tuples, document_names, vocab)
rareword = 'dagger'
rareidx = vocab.index(rareword)
freqword = 'run'
freqidx = vocab.index(freqword)
play = 'Julius Caesar'
playidx = document_names.index(play)
try:
    student_tfidf_matrix = main.create_tf_idf_matrix(soln_term_doc_matrix)
    rare_tfidf = student_tfidf_matrix[rareidx,playidx]
    freq_tfidf = student_tfidf_matrix[freqidx,playidx]
except AttributeError:
    student_tfidf_matrix = main.compute_tf_idf_matrix(soln_term_doc_matrix)
    rare_tfidf = student_tfidf_matrix[rareidx,playidx]
    freq_tfidf = student_tfidf_matrix[freqidx,playidx]
except Exception as e:
    print('Could not call create_tf_idf_matrix')
    print(str(e))
    rare_tfidf = -1
    freq_tfidf = -1

if not rare_tfidf > freq_tfidf:
    print('TF-IDF for frequent word %s, play %s is greater than TF-IDF for rare word %s, play %s; should be less.\n' % (freqword, play, rareword, play))
else: print('Correct!')


"""Check values in PPMI matrix for first 1k vocab words"""
print('1.4')
shortvocab = vocab[:N]
for word in ['dagger','run','the','bloody','sword']:
    if word not in shortvocab:
        shortvocab.append(word)

soln_term_ctx_matrix = main_solutions.create_term_context_matrix(tuples, shortvocab, context_window_size=2)
freqctx = 'the'
freqidx = shortvocab.index(freqctx)
rarectx = 'bloody'
rareidx = shortvocab.index(rarectx)
noun = 'sword'
nnidx = shortvocab.index(noun)
try:
    student_ppmi_matrix = main.create_PPMI_matrix(soln_term_ctx_matrix)
    rare_ppmi = student_ppmi_matrix[rareidx,nnidx]
    freq_ppmi = student_ppmi_matrix[freqidx,nnidx]
except Exception as e:
    print('Could not call create_PPMI_matrix')
    print(str(e))
    rare_ppmi = -1
    freq_ppmi = -1
if not rare_ppmi > freq_ppmi:
    print('PPMI for frequent context %s, word %s is greater than PPMI for rare context %s, word %s; should be less.\n' % (freqctx, noun, rarectx, noun))
else: print('Correct!')


"""Check result of cosine similarity fn"""
print('1.5')
v_i = np.random.uniform(0, 1, (3,))
v_j = np.random.uniform(0, 1, (3,))
student_cos = np.around(main.compute_cosine_similarity(v_i, v_j), 4)
soln_cos = np.around(main_solutions.compute_cosine_similarity(v_i, v_j), 4)
if student_cos!=soln_cos:
    print('Incorrect value for cosine similarity of vectors %s and %s: got %0.4f, should be %0.4f' % (str(v_i), str(v_j), student_cos, soln_cos))
else: print('Correct!')

"""Check result of jaccard similarity fn"""
print('1.6')
v_i = np.random.uniform(0, 1, (3,))
v_j = np.random.uniform(0, 1, (3,))
student_jac = np.around(main.compute_jaccard_similarity(v_i, v_j), 4)
soln_jac = np.around(main_solutions.compute_jaccard_similarity(v_i, v_j), 4)
if student_jac!=soln_jac:
    print('Incorrect value for jaccard similarity of vectors %s and %s: got %0.4f, should be %0.4f' % (str(v_i), str(v_j), student_jac, soln_jac))
else: print('Correct!')


"""Check result of dice similarity fn"""
print('1.7')
v_i = np.random.uniform(0, 1, (3,))
v_j = np.random.uniform(0, 1, (3,))
student_dice = np.around(main.compute_dice_similarity(v_i, v_j), 4)
soln_dice = np.around(main_solutions.compute_dice_similarity(v_i, v_j), 4)
if student_dice!=soln_dice:
    print('Incorrect value for dice similarity of vectors %s and %s: got %0.4f, should be %0.4f' % (str(v_i), str(v_j), student_dice, soln_dice))
else:
    print('Correct!')



"""Check most-similar play to randomly selected play (excluding self)"""
print('1.8')
soln_term_doc_matrix = main_solutions.create_term_document_matrix(tuples, document_names, vocab)
soln_tfidf_matrix = main_solutions.create_tf_idf_matrix(soln_term_doc_matrix)
tgt_play = 'Richard III'
i = document_names.index(tgt_play)
student_ranking = main.rank_plays(i, soln_tfidf_matrix, main_solutions.compute_cosine_similarity)
soln_ranking = main_solutions.rank_plays(i, soln_tfidf_matrix, main_solutions.compute_cosine_similarity)
student_n2 = document_names[student_ranking[1]]
soln_n2 = document_names[soln_ranking[1]]
if student_n2 != soln_n2:
    print('Incorrect most-similar play to %s, computed using tf-idf matrix with cosine similarity: got %s, should be %s' % (tgt_play, student_n2, soln_n2))
else: print('Correct!')


"""Check most-similar word to randomly selected word (excluding self)"""
print('1.9')
shortvocab = vocab[:N]
soln_term_ctx_matrix = main_solutions.create_term_context_matrix(tuples, shortvocab, context_window_size=2)
soln_ppmi_matrix = main_solutions.create_PPMI_matrix(soln_term_ctx_matrix)
tgt_word = 'sword'
i = shortvocab.index(tgt_word)
student_ranking = main.rank_words(i, soln_ppmi_matrix, main_solutions.compute_cosine_similarity)
student_n2 = shortvocab[student_ranking[1]]
if student_n2!='dagger':
    print('Incorrect most-similar word to %s, computed using PPMI matrix with cosine similarity: got %s, should be %s' % (tgt_word, student_n2, 'dagger'))
else:
    print('Correct!')
