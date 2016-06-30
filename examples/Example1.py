from iAlignment.iAligner import iAligner
from iAlignment.Viewer import Viewer

#Example 1: simple alignment, align two sentences
sentence1="And the earth was waste and void; and darkness was upon the face of the deep: and the Spirit of God moved upon the face of the waters. And God said, Let there be light: and there was light."
sentence2="And the earth was waste and without form; and it was dark on the face of the deep: and the Spirit of God was moving on the face of the waters. And God said, Let there be light: and there was light."

aligner = iAligner()
# alignment options /
aligner.setOptions(1,0,1,0)
viewer = Viewer()

# run the alignment
alignment = aligner.align(sentence1, sentence2)

# view the alignment results in html table
html=viewer.alignmentToText(alignment)
html+=viewer.alignmentToHtmlCode(alignment)
viewer.exportHtml(html,"outputExample1.html") #"<br>".join(text)
