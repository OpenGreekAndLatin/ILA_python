#!/usr/bin/python
# -*- coding: UTF-8 -*-
import webbrowser
import os.path
class Viewer:
    templatefile="templates/header.html"
    def __init__(self):
        print("Class Viewer")

    def alignmentToHTML(self, alignment):
        header=[]
        f=open(os.path.realpath(self.templatefile),"r")
        content=f.read()
        f.close()
        s1=[]
        s2=[]

        for r in alignment:
            styleclass = "<td class='danger'>"
            if r['relation']=="Aligned":
                styleclass = "<td class='success'>"

            s1.append("".join([styleclass,r['sentence1'],"</td>"]))
            s2.append("".join([styleclass,r['sentence2'],"</td>"]))

        html="".join(["<table class='table'><tr>","".join(s1),"</tr><tr>","".join(s2),"</tr></table>"])
        content=content.replace("[REPLACE]",html)

        f=open("test.html","w")
        f.write(content)
        f.close()
        webbrowser.open("file://"+os.path.realpath("test.html"))


