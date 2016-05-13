" Sentence Class"
import re
class Sentence:
    'Documentation'

    def __init__(self,te="",tok=[]):
        self.text=te
        self.tokens=tok
        self.setText(te)

    def setText(self,te):
        te=re.sub( '\s+', ' ', te ).strip() #replace myltiple whitespaces withs single white space
        self.text=te
        if "||" in self.text.split(' '):
            print("|| found")
            self.WStokenizer()
        else:
            self.AdvancedTokenizer()

    def WStokenizer(self):
        self.tokens=self.text.split(' ')     

        
    def AdvancedTokenizer(self):
        original=['”'  , '“' , '؛' , '،' , "." , "," , ":" , ";" , "[" , "]" , "(" , ")" , "{" , "}" , "\"" , "'" , "\“" , "?" , "!" ]
        replacement=[' " ',' " ',' ; ',' , '," . "," , "," : "," ; "," [ "," ] "," ( "," ) "," { "," } "," \" "," ' "," \“ "," ? "," ! "]
        for i in range(0,len(original)):
            self.text=self.text.replace(original[i],replacement[i])
        self.text=re.sub( '\s+', ' ',self.text ).strip()
        self.tokens=self.text.split(' ')


        
