import pandas as pd
import scipy.stats as stats
from pymagnitude import *


def main():
    vectors = Magnitude('GoogleNews-vectors-negative300.magnitude')
    df = pd.read_csv('data/SimLex-999.txt', sep='\t')[['word1', 'word2', 'SimLex999']]
    human_scores = []
    vector_scores = []
    for word1, word2, score in df.values.tolist():
        human_scores.append(score)
        similarity_score = vectors.similarity(word1, word2)
        vector_scores.append(similarity_score)
        print(f'{word1},{word2},{score},{similarity_score:.4f}')

    correlation, p_value = stats.kendalltau(human_scores, vector_scores)
    print(f'Correlation = {correlation}, P Value = {p_value}')


if __name__ == '__main__':
    main()
