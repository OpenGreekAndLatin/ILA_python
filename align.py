import sys
import os.path
from models.iAligner import iAligner
from models.Viewer import Viewer

#read command line arguments
args=sys.argv
inpt=""
outpt=""



#first parameter is the input file
# the input should be in CSV format
try:
    inpt=args[1]
except IndexError:
    print("There is no input file")
    sys.exit()

#second parameter is the output file
try:
    outpt = args[2]
except IndexError:
    outpt=os.path.dirname(os.path.realpath(__file__))

print("Input: "+os.path.realpath(inpt))
print("Output: "+outpt)

#read the input file
f=open(os.path.realpath(inpt), "r")
lines = f.readlines()
f.close()

#declare an aligner
aligner=iAligner()
viewer=Viewer()
html=[]
resources= lines[0]
for line in lines[1:]:
    sentences=line.split("\t")
    alignment = aligner.align(sentences[0], sentences[1])
    html.append(viewer.alignmentToHtmlCode(alignment))
viewer.exportHtml("<br>".join(html))



