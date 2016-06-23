#!/usr/bin/python
# -*- coding: UTF-8 -*-
import webbrowser
import os.path


class Viewer:
    templatefile="./templates/header.html"

    # default constuctor
    def __init__(self):
        self.templatefile = "../templates/header.html"

    # pairwise alignment as a table exported in html file=outputfile
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

    # pairwise alignment as html code
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

    # export the result as html file
    def exportHtml(self, html, outputfile="test.html"):
        f=open(os.path.realpath(self.templatefile),"r")
        content=f.read()
        f.close()
        content = content.replace("[REPLACE]", html)
        f = open(outputfile, "w")
        f.write(content)
        f.close()
        webbrowser.open("file://" + os.path.realpath(outputfile))

    # this function assign colors to each cell in the alignment table according to other aligned tokens in the same column
    def coloring(self,vector):
        distinctColors=dict()
        colors=dict()
        for v in vector:
            if v in distinctColors:
                distinctColors[v] += 1
            else:
                distinctColors[v] = 1
        counter=0
        colorSet = ["#DFF0DA", "#CCFFAA", "#DDFFCC", "#DDEEDD", "#EEEEDD"]
        singleColor="#f2dede"
        for k in distinctColors:
            if distinctColors[k]==1 or k=="":
                colors[k]=singleColor
            else:
                if counter >= len(colorSet):
                    counter=0
                colors[k]=colorSet[counter]
                counter+=1

        ret=dict()
        for i in range(len(vector)):
            ret[vector[i]]=colors[vector[i]]
        return ret

    # show the alignment of multiple sentences as html table
    def mAlignmentToHtmlCode(self,txt,sentences):
        arr=self.getArray(txt)
        table=["" for x in range(len(sentences))]  #reset Matrix Variable
        for vector in arr:
            coloredcolumns=self.coloring(vector)
            c=0
            for col in vector:
                table[c]+="<td bgcolor='" + coloredcolumns[col] +"'>"+ col +"</td>"
                c=c+1
        table.reverse()
        html="<table class='table' ><tr>" + "</tr><tr>".join(table) + "</tr></table>"
        return html

    def getArray(self, txt):
        arr = txt.split(" ")
        tds = []
        for v in arr:
            cells = v.split("||")
            cells.reverse()
            tds.append(cells)
        return tds

    # function to sort a dictionary and maitain idex association
    def asort(dd):
        return sorted(dd.items(), key=lambda x: x[1], reverse=True)