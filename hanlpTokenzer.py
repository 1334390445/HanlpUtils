#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/3/1 21:19
@Author : Administrator
@Email : xxxxxxxxx@qq.com
@File : hanlpTokenzer.py
@Project : untitled
"""
from jpype import *
from HanlpUtils import Config
hanlp_path=Config.HANLP_PATH
startJVM(getDefaultJVMPath(), '-Djava.class.path={}'.format(hanlp_path),
             "-Xms1g",
             "-Xmx1g"
             )

class HanlpTokenzer(object):

    def __init__(self):
        pass

    def JClass(self,jclass="HanLP"):
        """
        hanlp常用的6种分词方法，分别"HanLP"、"StandardTokenizer"、"NLPTokenizer"、"IndexTokenizer"、"SpeedTokenizer"、"CustomDictionary"
        :param jclass: 对应分词器的java类
        :return: obj    分词器对象
        """
        if jclass == "HanLP":
            # Hanlp分词
            obj = JClass('com.hankcs.hanlp.HanLP')
        elif jclass == "StandardTokenizer":
            # "标准分词"
            obj = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
        elif jclass == "NLPTokenizer":
            # NLP分词NLPTokenizer会执行全部命名实体识别和词性标注
            obj = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
        elif jclass == "IndexTokenizer":
            # 索引分词
            obj = JClass('com.hankcs.hanlp.tokenizer.IndexTokenizer')
        elif jclass == "SpeedTokenizer":
            # 极速词典分词
            obj = JClass('com.hankcs.hanlp.tokenizer.SpeedTokenizer')
        elif jclass == "CustomDictionary":
            # 自定义分词
            obj = JClass('com.hankcs.hanlp.dictionary.CustomDictionary')
        else:
            if jclass is not None:
                try:
                    obj = JClass(jclass)  #默认
                except Exception as e:
                    raise e
        return obj


    def load_stopwords(self,stopwordspath):
        """
        加载自定义停词的文件
        :param stopwordspath: 
        :return: stopword
        """
        try:
            stopwords = [line.rstrip() for line in open(stopwordspath, "r", encoding='utf-8')]
        except Exception as e:
            raise e
        else:
            return stopwords

    def load_keepwords(self, keepwordspath):
        """
        加载自定义保留词性的文件
        :param keepwordspath: 
        :return: 
        """
        try:
            keepwords = [line.rstrip() for line in open(keepwordspath, "r", encoding='utf-8')]
        except Exception as e:
            raise e
        else:
            return keepwords



    def stopwords(self,word_pos_list,split='/',stopwords=None,iterable=False):
        """
        过滤调指定词性的词汇
        :param word_pos_list: 
        :param split: 
        :param stopwords: 
        :param iterable: 
        :return: 
        """
        if len(word_pos_list) > 0:
            try:
                new_word_pos_list = [str(word_pos) for word_pos in word_pos_list
                                     if len(str(word_pos).split(split)) == 2
                                     and str(word_pos).split(split)[1]
                                     not in stopwords
                                     ]

                if iterable:
                    return iter(new_word_pos_list)
                else:
                    return new_word_pos_list

            except Exception as e:
                raise e

    def keepwords(self,word_pos_list,split='/',keepwords=None,iterable=False):
        """
        过滤调指定词性的词汇
        :param word_pos_list: 
        :param split: 
        :param keepwords: 
        :param iterable: 
        :return: 
        """
        if len(word_pos_list) > 0:
            try:
                new_word_pos_list = [str(word_pos) for word_pos in word_pos_list
                                     if len(str(word_pos).split(split)) == 2
                                     and str(word_pos).split(split)[1] in keepwords
                                     ]

                if iterable:
                    return iter(new_word_pos_list)
                else:
                    return new_word_pos_list

            except Exception as e:
                raise e
