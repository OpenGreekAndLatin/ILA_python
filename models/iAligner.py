from .Token import Token
from .Sentence import Sentence

class iAligner:

    token=Token()
    sentence1=Sentence()
    sentence2=Sentence()
    #Alignment Options
    NonAlphanumeric = 0
    casesensitive = 0
    diacritics = 0
    levenshtein = 0

    # this variables will be ued in Needlman - Wunsch Algorithm
    # Changing these values will produce different result
    gap = -2
    mismatch = -2
    match = 5

    matrix = []
    optimal_alignment = []

    def __init__(self,sentence1,sentence2):
        self.sentence1.setText(sentence1.strip())
        self.sentence2.setText(sentence2.strip())

    def setSentences(self,s1,s2):
        self.sentence1.setText(s1.strip())
        self.sentence2.setText(s2.strip())

    def setOptions(self,punc=1,case=0,diac=1,lev=0):
        self.NonAlphanumeric=punc
        self.casesensitive=case
        self.diacritics=diac
        self.levenshtein=lev

    def initialization(self):

        m= len(self.sentence1.tokens)
        n= len(self.sentence2.tokens)
        self.matrix=[[{'val':0,'pointer':''} for x in range(n+1)] for y in range(m+1)]  #reset Matrix Variable
        for i in range(m):
            self.matrix[i + 1][0]['val'] = (i+1)*self.gap
        for i in range(n):
            self.matrix[0][i + 1]['val'] = (i+1)*self.gap

    def fillMatrix(self):
        m = len(self.sentence1.tokens)
        n = len(self.sentence2.tokens)
        for i in range(1,m+1):
            for j in range(1,n+1):
                sc=self.mismatch
                if self.isAligned(self.sentence1.tokens[i-1],self.sentence2.tokens[j-1]):
                    sc=self.match
                ma=self.matrix[i][j]['val']+sc
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



    # very simple : should be reimplemented
    def isAligned(self,w1,w2):
        w1=w1.strip()
        w2=w2.strip()
        if w1==w2:
            return True
        else:
            return False



    def printArray(self):
        m= len(self.sentence1.tokens)
        n= len(self.sentence2.tokens)
        print(self.sentence1.tokens)
        print(self.sentence2.tokens)
        print(m)
        print(n)
        print(self.matrix)
        for i in range(m+1):
            for j in range(n+1):
                print(self.matrix[i][j])

