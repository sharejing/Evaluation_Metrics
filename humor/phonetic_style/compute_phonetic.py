"""
---------------------------------------------
  File Name:    compute_phonetic
  Description:  计算每一个句子的发音类型
  Author:       nycolas
  Date:         18-3-28
---------------------------------------------

"""

from pypinyin import pinyin, lazy_pinyin, STYLE_TONE2

# print(pinyin('今天真好呀！'))
#
# print(lazy_pinyin('今天真好呀！'))
import string

def compute_pinyin(sentence):

    p = 0

    # 少一步去除所有标点符号
    pinyin_list = lazy_pinyin(sentence, style=STYLE_TONE2)

    # for key in pinyin_list:
    #
    #     if
    print(pinyin_list)
compute_pinyin('今天真好呀！')