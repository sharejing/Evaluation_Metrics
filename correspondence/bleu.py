"""
---------------------------------------------
  File Name:    bleu
  Description:  默认计算BLEU-4值
  Author:       nycolas
  Date:         18-3-30
---------------------------------------------

"""

from nltk.translate.bleu_score import corpus_bleu
from nltk.translate.bleu_score import SmoothingFunction

smoothie = SmoothingFunction().method4

reference = open('data/reference.txt', 'r')
pred = open('data/pred.txt', 'r')
reference_iter = iter(reference)
pred_iter = iter(pred)

list_of_references = []
hypotheses = []

for line in reference_iter:

    re_list = line.strip().split(' ')
    list_of_references.append([re_list])

for line in pred_iter:

    pe_list = line.strip().split(' ')

    hypotheses.append(pe_list)

# score_1 = corpus_bleu(list_of_references, hypotheses, weights=(1, 0, 0, 0), smoothing_function=smoothie)
#
# score_2 = corpus_bleu(list_of_references, hypotheses, weights=(0.5, 0.5, 0, 0), smoothing_function=smoothie)
#
# score_3 = corpus_bleu(list_of_references, hypotheses, weights=(0.33, 0.33, 0.33, 0), smoothing_function=smoothie)
#
# score_4 = corpus_bleu(list_of_references, hypotheses, weights=(0.25, 0.25, 0.25, 0.25), smoothing_function=smoothie)
#
# print("BLEU1 Score = " + str(100*score_1))
# print("BLEU2 Score = " + str(100*score_2))
# print("BLEU3 Score = " + str(100*score_3))
# print("BLEU4 Score = " + str(100*score_4))

score = corpus_bleu(list_of_references, hypotheses)   # 默认计算BLEU-4值

print("BLEU4 Score = " + str(100*score))

reference.close()
pred.close()

