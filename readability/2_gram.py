"""
---------------------------------------------
  File Name:    2_gram
  Description:
  Author:       nycolas
  Date:         18-3-30
---------------------------------------------

"""

import math


def count_word():

    single_word = {}
    bi_word = {}
    bi_list = []

    data = open('data/2_gram_jokes', 'r').readlines()
    for line in data:
        words = line.strip().split(' ')
        for word in words:
            if word not  in single_word:
                single_word[word] = 1
            else:
                single_word[word] += 1

        for i in range(len(words) - 1):
            bi_list.append((words[i], words[i+1]))
    for bi in bi_list:
        if bi not in bi_word:
            bi_word[bi] = 1
        else:
            bi_word[bi] += 1

    return single_word, bi_word

single_word, bi_word = count_word()


def compute_p(sentence):

    words = sentence.strip().split(' ')
    p = 0

    for j in range(len(words) - 1):
        if (words[j], words[j+1]) not in bi_word:
            p = p - 0.0005

        else:
            p  = p + math.log( bi_word[(words[j], words[j+1])] / single_word[words[j]])

    return p

p = compute_p('我 应该 努力 学习')
print(p)