"""
---------------------------------------------
  File Name:    compute_ambiguity
  Description:  计算每一个句子的模糊性
  Author:       nycolas
  Date:         18-3-28
---------------------------------------------

"""
import jieba.posseg as psg
import math


data = open('data/HowNet_Chinese_WordList', 'r')
iter_data = iter(data)

dict = {}

for line in iter_data:
    list = line.strip().split(' ')
    if len(list) == 2:
        dict[list[0]] = int(list[1])

data.close()


def compute_a(sentence):
    p = 0
    for key in psg.cut(sentence):
        if key.flag in ['n', 'a', 'd', 'v']:
            if key.word in dict:

                print(key.word, dict[key.word])
                p = p + math.log(dict[key.word])
    return p


p1 = compute_a('今天真是一个好天气呀!')
p2 = compute_a('我需要方便一下')

print(p1, p2)

