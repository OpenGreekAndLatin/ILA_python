" Token Class "
import re

class Token:
    'Documentation should be written'

    

    @classmethod
    def removeDiacritics(self, tok):

        return tok
    
    @classmethod
    def removeNonAlphanumeric(self, tok):
        '$temp=preg_replace("/\P{L}+/u", " ", $token); // replace non letter charecters with whitespace'
        temp=''.join([i for i in tok if i.isalpha() or i is " "])    # replace non letter characters with whitespace
        return temp.replace("  "," ").strip()                       # replace double whitespaces with single whitespace

    @classmethod
    def lowercase(self, tok):
        return tok.lower()

    @classmethod
    def isSimilarto(self, tok1, tok2):
        'Levenshtein method, this method will be implemented later'
        return True


        # testing
#t= Token()
#print(t.removeNonAlphanumeric("Hi, How are you doing??"))
