#testing
from models.iAligner import iAligner

al=iAligner("How are you doing","How are you doing my dear")
al.initialization()
al.fillMatrix()
al.printArray()
