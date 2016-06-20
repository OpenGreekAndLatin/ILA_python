import sys
import os.path
from models.iAligner import iAligner
from models.Viewer import Viewer

#read command line arguments
args=sys.argv
inpt=""
outpt=""

#first parameter is the input file
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
f=open(os.path.realpath(inpt),"r")
content=f.read()
f.close()

#declare an aligner
al=iAligner()
viewer=Viewer()

