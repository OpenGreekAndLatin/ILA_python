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

    def __init__(self,sentence1="",sentence2=""):
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
        self.matrix=[[{'val':0,'pointer':'NW'} for x in range(n+1)] for y in range(m+1)]  #reset Matrix Variable
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


    def getOptimalAlignment(self):
        m = len(self.sentence1.tokens)
        n = len(self.sentence2.tokens)

        i=m
        j=n
        while i >=0 and j>=0:
            base1=self.sentence1.tokens[i-1]
            base2=self.sentence2.tokens[j-1]
            pointer=self.matrix[i][j]['pointer']

            if pointer=="NW":
                i-=1
                j-=1
                if self.isAligned(base1,base2):
                    self.optimal_alignment.append({'sentence1': base1, 'sentence2': base2, 'relation': "Aligned"})
                else:
                    self.optimal_alignment.append({'sentence1': base1, 'sentence2': base2, 'relation': "Not Aligned"})
            elif pointer=="LE":
                j-=1
                self.optimal_alignment.append({'sentence1': "", 'sentence2': base2, 'relation': "Not Aligned"})
            elif pointer=="UP":
                i-=1
                self.optimal_alignment.append({'sentence1': base1, 'sentence2': "", 'relation': "Not Aligned"})

        if i < 0:
            while j >= 0:
                base2 = self.sentence2.tokens[j-1]
                j-=1
                self.optimal_alignment.append({'sentence1': "", 'sentence2': base2, 'relation': "Not Aligned"})
        if j < 0 :
            while i >= 0 :
                base1 = self.sentence1.tokens[j-1]
                i-=1
                self.optimal_alignment.append({'sentence1': base1, 'sentence2': "", 'relation': "Not Aligned"})

        self.optimal_alignment.reverse()



    # PairwaiseAlignment: align two sentences

    def align(self, sen1, sen2):
        self.setSentences(sen1,sen2)
        self.initialization()
        self.fillMatrix()
        self.getOptimalAlignment()
        self.printArray()
        return self.optimal_alignment



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
        columns=["",""]+self.sentence2.tokens
        rows=[""]+self.sentence1.tokens

        output=[]

        print("  \t|\t  ".join(columns))
        for i in range(m+1):
            output=[]
            output.append(rows[i])
            for j in range(n+1):
                output.append(("%s (%s)" % (self.matrix[i][j]['val'],self.matrix[i][j]['pointer'])))
            print("\t|\t".join(output))
            print("\n")

    def printMatrix(self):
        m= len(self.sentence1.tokens)
        n= len(self.sentence2.tokens)
        columns=["",""]+self.sentence2.tokens
        rows=[""]+self.sentence1.tokens

        output=[]

        html="<td></td>".join(columns)
        for i in range(m+1):
            output=[]
            output.append(rows[i])
            for j in range(n+1):
                output.append(("%s (%s)" % (self.matrix[i][j]['val'],self.matrix[i][j]['pointer'])))
            print("\t|\t".join(output))
            print("\n")
