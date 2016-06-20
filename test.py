#testing
from models.iAligner import iAligner
from models.Viewer import Viewer
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

al=iAligner()
viewer=Viewer()
res=al.align("How ar you my","How are you doing my dear")
viewer.alignmentToHTML(res)
