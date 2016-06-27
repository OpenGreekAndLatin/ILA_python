#!/usr/bin/python
# -*- coding: UTF-8 -*-

" Token Class "
import re


class Token:
    'Documentation should be written'

    

    @classmethod
    def removeDiacritics(self, tok):
        original = ["ῆ", "ῒ", "ῒ", "ῖ", "ῶ", "ά", "ά", "ὰ", "έ", "ὲ", "ή", "ὴ", "ί", "ὶ", "ό", "ό", "ὸ", "ύ", "ὺ",
                          "ώ", "ὼ", "ᾴ", "ᾲ", "ῄ", "ῂ", "ῴ", "ῲ", "Ά", "Ὰ", "Έ", "Ὲ", "Ὴ", "Ή", "Ί", "Ὶ", "Ὸ", "Ό", "Ύ",
                          "Ὺ", "Ώ", "Ὼ"]
        replacement = ["η", "ι", "ι", "ι", "ω", "α", "α", "α", "ε", "ε", "η", "η", "ι", "ι", "ο", "ο", "ο", "υ",
                             "υ", "ω", "ω", "ᾳ", "ᾳ", "ῃ", "ῃ", "ῳ", "ῳ", "Α", "Α", "Ε", "Ε", "Η", "Η", "Ι", "Ι", "Ο",
                             "Ο", "Υ", "Υ", "Ω", "Ω"]
        for i in range(0,len(original)):
            tok=tok.replace(original[i],replacement[i])
        return tok

    
    @classmethod
    def removeNonAlphanumeric(self, tok):
        temp=''.join([i for i in tok if i.isalpha() or i is " "])    # replace non letter characters with whitespace
        return temp.replace("  "," ").strip()                       # replace double whitespaces with single whitespace

    @classmethod
    def lowercase(self, tok):
        return tok.lower()

    @classmethod
    def isSimilarto(self, tok1, tok2):
        'Levenshtein method, this method will be implemented later'
        m = len(tok1)
        n = len(tok2)
        lensum = float(m + n)
        d = []
        for i in range(m + 1):
            d.append([i])
        del d[0][0]
        for j in range(n + 1):
            d[0].append(j)
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if tok1[i - 1] == tok2[j - 1]:
                    d[i].insert(j, d[i - 1][j - 1])
                else:
                    minimum = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + 2)
                    d[i].insert(j, minimum)
        ldist = d[-1][-1]
        ratio = (lensum - ldist) / lensum
        return (ratio > 0.66)

