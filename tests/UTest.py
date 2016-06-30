#!/usr/bin/python
# -*- coding: UTF-8 -*-
from unittest import TestCase
from iAlignment.Sentence import Sentence
from iAlignment.Token import Token
from iAlignment.iAligner import iAligner
from iAlignment.MultipleAligner import MultipleAligner


class UTest(TestCase):

    def setUp(self):
        self.sentence = Sentence("How are you?")
        self.aligner = iAligner()
        self.maligner = MultipleAligner()

    def testSentence(self):
        """ Ensure Sentences methods are working well """
        expectedResult = ["How", "are", "you", "?"]
        expectedResult2 = ["How", "are", "you?"]
        # check if the advanced tokenizer is working
        self.assertEqual(
            self.sentence.AdvancedTokenizer(), expectedResult,
            "AdvancedTokenizer should separate punctuation marks from word strings"
        )
        # check if the advanced tokenizer is working
        self.assertEqual(
            self.sentence.WStokenizer(), expectedResult2,
            "WhiteSpace tokenizer should separate only on whitespaces"
        )

    def testToken(self):
        """ Ensure Token's methods are working well """
        # check if lowercase(work) function is working
        self.assertEqual(Token.lowercase("LEIPZIG"),"leipzig","converting the toke to lowercase is not working")
        # check if removeNonAlphanumeric(word) is working
        self.assertEqual(Token.removeNonAlphanumeric("{,Leipzig?}"),"Leipzig" ,"remove of none alphabitical charachters is not working")
        # check if levenshtein distance metric is working
        # leiozig ~ leipzen are approximately simlar according to the similarity threshold given in the Token class
        self.assertTrue(Token.isSimilarto("leipzig","leipzen"), "Levenshtein similarity is not working")
        # check if removeDiacritics(word) is working
        self.assertEqual(Token.removeDiacritics("ῆὲῶ"),"ηεω" ,"remove of diacritics is not working")

    def testiAligner(self):
        self.aligner.setOptions(1,0,1,1)
        alignment = self.aligner.align("How are you doing?","what Are YOU doing")
        self.assertIn({"sentence1": "are", "sentence2": "Are", "relation": "Aligned"},alignment)
        self.assertIn({"sentence1": "How", "sentence2": "what", "relation": "Not Aligned"},alignment)

    #def testMultipleAligner(self):






