#!/usr/bin/python
# -*- coding: UTF-8 -*-

from iAlignment.iAligner import iAligner
from iAlignment.Token import Token

class MultipleAligner(iAligner):

    def __init__(self):
        self.token=Token()


    def align(self, sentences):
        n=len(sentences)
        if n > 1:
            alignment=super(MultipleAligner,self).align(sentences[0],sentences[1])
            sen12=[]
            newSentences=[]
            for couple in alignment:
                sen12.append("||".join([couple['sentence1'],couple['sentence2']]))
            newSentences.append(" ".join(sen12))
            for i in range(2,n):
                newSentences.append(sentences[i])
            return self.align(newSentences)
        else:
            #print(sentences[0])
            return self.getArray(sentences[0])



    def fillMatrix(self):
        m = len(self.sentence1.tokens)
        n = len(self.sentence2.tokens)
        for i in range(1,m+1):
            tokens12=self.sentence1.tokens[i-1].split("||")
            for j in range(1,n+1):
                sc=self.mismatch
                if self.isAligned_multi(tokens12,self.sentence2.tokens[j-1]):
                    sc=self.match
                ma=self.matrix[i-1][j-1]['val']+sc
                hgap = self.matrix[i - 1][j]['val'] + self.gap
                vgap = self.matrix[i][j - 1]['val'] + self.gap
                MaxValue=max(ma,hgap,vgap)
                pointer="NW"
                if MaxValue==hgap and MaxValue > ma:
                    pointer="UP"
                elif MaxValue==vgap and MaxValue > ma:
                    pointer="LE"

                self.matrix[i][j]['val']=MaxValue
                self.matrix[i][j]['pointer']=pointer


    def isAligned_multi(self,tokenArr,token):
        aligned=False
        for t in tokenArr:
            if self.isAligned(token,t):
                aligned=True
        return aligned


    def getArray(self, txt):
        arr = txt.split(" ")
        tds = []
        ret=[]
        maxsize=0
        for v in arr:
            cells = v.split("||")
            #cells.reverse()
            if maxsize < len(cells):
                maxsize=len(cells)
            tds.append(cells)

        for column in tds:
            if len(column) < maxsize:
                temp=["" for x in range (maxsize-len(column))]
                column= temp +column
            column.reverse()
            ret.append(column)
        return ret


