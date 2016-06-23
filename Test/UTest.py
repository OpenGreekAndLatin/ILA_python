from unittest import TestCase
from models.Sentence import Sentence
from models.Token import Token
class UTest(TestCase):

    def setUp(self):
        self.sentence=Sentence("How are you?")


    def testSentence(self):
        expectedResult=["How","are","you","?"]
        expectedResult2=["How","are","you?"]
        self.assertEqual(self.sentence.AdvancedTokenizer(),expectedResult,"AdvancedTokenizer is not working well")
        self.assertEqual(self.sentence.WStokenizer(), expectedResult2, "WhiteSpace tokenizer is not working well")

    def testToken(self):
        self.assertEqual(Token.lowercase("LEIPZIG"),"leipzig","converting the toke to lowercase is not working")
        self.assertEqual(Token.removeNonAlphanumeric("{,Leipzig?}"),"Leipzig" ,"remove of none alphabitical charachters is not working")
        self.assertTrue(Token.isSimilarto("leipzig","leipzen"), "Levenshtein similarity is not working")
        self.assertEqual(Token.removeDiacritics("ῆὲῶ"),"ηεω" ,"remove of diacritics is not working")







