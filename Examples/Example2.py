from models.iAligner import iAligner
from models.Viewer import Viewer
import os.path

#Example 2: read parallel sentences from CSV file
# sen1_trans1   sen1_trans2 sen1_trans3
# sen2_trans1   sen2_trans2 sen2_trans3

filepath="example2.csv"
aligner = iAligner()
viewer = Viewer()

#read the input file
f=open(os.path.realpath(filepath), "r")
lines = f.readlines()
f.close()

html=[]
resources= lines[0]
for line in lines[1:]:
    sentences=line.split("\t")
    alignment = aligner.align(sentences[0], sentences[1])
    html.append(viewer.alignmentToHtmlCode(alignment))
viewer.exportHtml("<br>".join(html))

