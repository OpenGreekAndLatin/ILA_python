from models.iAligner import iAligner
from models.Viewer import Viewer
from models.MultipleAligner import MultipleAligner
import os.path

#Example 4: read parallel sentences from CSV file
# sen1_trans1   sen1_trans2 sen1_trans3
# sen2_trans1   sen2_trans2 sen2_trans3

filepath="data/example2.csv"
aligner = MultipleAligner()
viewer = Viewer()

#read the input file
f=open(os.path.realpath(filepath), "r")
lines = f.readlines()
f.close()

html=[]
resources= lines[0]
for line in lines[1:]:
    sentences=line.split("\t")
    alignment = aligner.align(sentences)
    html.append(viewer.mAlignmentToHtmlCode(alignment,sentences))
viewer.exportHtml("<br>".join(html),"OutputExample3.html")

