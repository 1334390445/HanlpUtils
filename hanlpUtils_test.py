#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/3/1 22:19
@Author : Administrator
@Email : xxxxxxxxx@qq.com
@File : hanlpUtils_test.py
@Project : untitled
"""
import os,gc,re,sys
from HanlpUtils.hanlpTokenzer import HanlpTokenzer


hanlp = HanlpTokenzer()

tokenizer = hanlp.JClass("HanLP")
# seg=tokenizer.newSegment().enableNameRecognize(True)
# word_pos_list = seg.segment('维基解密网站创始人朱利安')
# print(str(word_pos_list))
# CustomDictionary=hanlp.JClass("CustomDictionary")
# CustomDictionary.add('C++','nx 5000')
# CustomDictionary.add('断网','o')
word_pos_list = tokenizer.segment("2、有丰富的数据挖掘\机器学习、自然语言处理、推荐算法等相关工作经验或者研究经历；")
word_pos_list2 = tokenizer.segment("3、良好的编程功底，熟悉Scala，至少精通C\C++\JAVA\PYTHON一门语言；")
print(word_pos_list)
print(word_pos_list2)


# stopwords = hanlp.load_stopwords(stopwordspath='keepwords.txt')
# new_word_pos_list = hanlp.stopwords(word_pos_list,stopwords=stopwords,iterable=False)
# print(new_word_pos_list)
#
# keepwords = hanlp.load_keepwords(keepwordspath='keepwords.txt')
# new_word_pos_list = hanlp.keepwords(word_pos_list,keepwords=keepwords,iterable=False)
# print(new_word_pos_list)

# core_swd = hanlp.JClass('com.hankcs.hanlp.dictionary.stopword.CoreStopWordDictionary')
# core_swd.apply(word_pos_list)
# print(str(word_pos_list))
#
# text = """
# "威廉王子发表演说 呼吁保护野生动物"
# "《时代》年度人物最终入围名单出炉 普京马云入选"
# "“黑格比”横扫菲：菲吸取“海燕”经验及早疏散"
# "日本保密法将正式生效 日媒指其损害国民知情权"
# "英报告说空气污染带来“公共健康危机”"
# """
#
#
# # Suggester = hanlp.JClass('com.hankcs.hanlp.suggest.Suggester')
# # print(dir(Suggester))
# # for line in text:
# #     Suggester.addSentence(line)
# #
# # Suggester.suggest("发言", 1)
#
# # print(tokenizer.parseDependency("把市场经济奉行的等价交换原则引入党的生活和国家机关政务活动中"))
# # from pyhanlp import *
#
# # 依存句法分析
#
# sentence = tokenizer.parseDependency('2、将算法应用到互联网海量数据中，解决公司核心机器学习问题，用户画像、个性化推荐等；')
# print(sentence)
#
# for word in sentence.iterator():  # 通过dir()可以查看sentence的方法
#     # print(word)
#     # print("%s --(%s)--> %s" % (word.LEMMA, word.DEPREL, word.HEAD.LEMMA))
#
# # 也可以直接拿到数组，任意顺序或逆序遍历
#
# word_array = sentence.getWordArray()
#
# for word in word_array:
#     print("%s --(%s)--> %s" % (word.LEMMA, word.DEPREL, word.HEAD.LEMMA))
#
#
#
# # 还可以直接遍历子树，从某棵子树的某个节点一路遍历到虚根
#
# CoNLLWord = hanlp.JClass("com.hankcs.hanlp.corpus.dependency.CoNll.CoNLLWord")
# for head in word_array:
#
#     while head.HEAD:
#         head = head.HEAD
#         if (head == CoNLLWord.ROOT):
#             pass
#             # print(head.LEMMA)
#         else:
#             print("%s --(%s)--> " % (head.LEMMA, head.DEPREL))
#
