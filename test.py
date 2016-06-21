#testing
from models.iAligner import iAligner
from models.Viewer import Viewer

sentence1="And the earth was waste and void; and darkness was upon the face of the deep: and the Spirit of God moved upon the face of the waters. And God said, Let there be light: and there was light."
sentence2="And the earth was waste and without form; and it was dark on the face of the deep: and the Spirit of God was moving on the face of the waters. And God said, Let there be light: and there was light."

aligner = iAligner()
viewer = Viewer()

alignment = aligner.align(sentence1, sentence2)
viewer.alignmentToHTML(alignment)
