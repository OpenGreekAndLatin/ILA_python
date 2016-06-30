#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Multiple Alignment

from iAlignment.iAligner import iAligner
from iAlignment.Viewer import Viewer
from iAlignment.MultipleAligner import MultipleAligner
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
print(alignment)
html=viewer.mAlignmentToHtmlCode(alignment,sentences)
viewer.exportHtml(html,"OutputExample3.html")