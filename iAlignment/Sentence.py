#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
class Sentence:

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
        return self.tokens

        
    def AdvancedTokenizer(self):
        original=['”'  , '“' , '؛' , '،' , "." , "," , ":" , ";" , "[" , "]" , "(" , ")" , "{" , "}" , "\"" , "'" , "\“" , "?" , "!" ]
        replacement=[' " ',' " ',' ; ',' , '," . "," , "," : "," ; "," [ "," ] "," ( "," ) "," { "," } "," \" "," ' "," \“ "," ? "," ! "]
        tempText=self.text
        for i in range(0,len(original)):
            tempText=tempText.replace(original[i],replacement[i])
        tempText=re.sub( '\s+', ' ',tempText ).strip()
        self.tokens=tempText.split(' ')
        return self.tokens