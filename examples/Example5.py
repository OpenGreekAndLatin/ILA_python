from iAlignment.Viewer import Viewer
from iAlignment.MultipleAligner import MultipleAligner
import os.path

#Example 4: read parallel sentences from text file
# sen1_trans1   sen1_trans2 sen1_trans3
# sen2_trans1   sen2_trans2 sen2_trans3

filepath="data/example5-1.txt"
aligner = MultipleAligner()
viewer = Viewer()
aligner.setOptions(1,0,0,1)
#read the input file
f=open(os.path.realpath(filepath), "r")
content = f.read()
f.close()

html=[]
groups=content.split("\n\n")
for group in groups:
    sentences=group.split("\n")
    alignment = aligner.align(sentences)
    html.append(viewer.mAlignmentToHtmlCode(alignment,sentences))
    html.append(viewer.mAlignmentToTableCode(alignment, sentences))
viewer.exportHtml("<br>".join(html),"OutputExample5-1.html")

