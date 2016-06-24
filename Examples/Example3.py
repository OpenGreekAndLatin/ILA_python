#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Multiple Alignment

from models.iAligner import iAligner
from models.Viewer import Viewer
from models.MultipleAligner import MultipleAligner
import os.path

sentence1="how are you doing"
sentence2="are you doing well"
sentence3="how are you ?"
sentence4="what are you doing"

sentences=[sentence1,sentence2,sentence3,sentence4]
viewer=Viewer()

mAlign=MultipleAligner()
mAlign.setOptions(1)
alignment=mAlign.align(sentences)
html=viewer.mAlignmentToHtmlCode(alignment,sentences)
viewer.exportHtml(html)