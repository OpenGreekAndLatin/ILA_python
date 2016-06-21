#!/usr/bin/python
# -*- coding: UTF-8 -*-
import webbrowser
import os.path
class Viewer:
    templatefile="../templates/header.html"
    def __init__(self):
        self.templatefile = "../templates/header.html"

    def alignmentToHTML(self, alignment, outputfile="test.html"):
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

        f=open(outputfile,"w")
        f.write(content)
        f.close()
        webbrowser.open("file://"+os.path.realpath(outputfile))



    def alignmentToHtmlCode(self,alignment):
        s1=[]
        s2=[]
        for r in alignment:
            styleclass = "<td class='danger'>"
            if r['relation'] == "Aligned":
                styleclass = "<td class='success'>"

            s1.append("".join([styleclass, r['sentence1'], "</td>"]))
            s2.append("".join([styleclass, r['sentence2'], "</td>"]))

        html = "".join(["<table class='table'><tr>", "".join(s1), "</tr><tr>", "".join(s2), "</tr></table>"])
        return html

    def exportHtml(self, html, outputfile="test.html"):
        f=open(os.path.realpath(self.templatefile),"r")
        content=f.read()
        f.close()
        content = content.replace("[REPLACE]", html)
        f = open(outputfile, "w")
        f.write(content)
        f.close()
        webbrowser.open("file://" + os.path.realpath(outputfile))

    def coloring(self,vector):
        colorSet=["#AED685","#CCFFAA","#DDFFCC","DDEEDD","EEEEDD"]
        singleColor="#F2A196"
        distinct=dict()
        colors=dict()
        for v in vector:
            if v in distinct:
                distinct[v] += 1
            else:
                distinct[v] = 1
        distinct=self.asort(distinct)
        counter=0
        for k in distinct:
            if distinct[k]==1:
                colors[k]=singleColor
            else:
                colors[k]=colorSet[counter]
                counter+=1
        ret=dict()




    def asort(d):
        return sorted(d.items(), key=lambda x: x[1], reverse=True)