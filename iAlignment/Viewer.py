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
            styleclass = "<td class='"+r['relation']+"'>"
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
        colorSet = ["#ACD689","#DFF0DA", "#CCFFAA", "#DDFFCC", "#DDEEDD", "#EEEEDD"]
        singleColor="#FA857D"
        gapColor="#F0F2D8"
        for k in distinctColors:
            if k=="":
                colors[k] = gapColor
            elif distinctColors[k]==1 :
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


    def coloring2(self,vector):
        distinctColors=dict()
        colors=dict()
        for v in vector:
            if v in distinctColors:
                distinctColors[v] += 1
            else:
                distinctColors[v] = 1
        counter=0
        colorSet = ["#3B9606","#DFF0DA", "#CCFFAA", "#DDFFCC", "#DDEEDD", "#EEEEDD"]
        singleColor="#F2362C"
        gapColor="#F2DB2C"
        for k in distinctColors:
            if k=="":
                colors[k] = gapColor
            elif distinctColors[k]==1 :
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
    def mAlignmentToHtmlCode(self,arr,sentences):
        table=["" for x in range(len(sentences))]  #reset Matrix Variable
        for vector in arr:
            coloredcolumns=self.coloring(vector)
            c=0
            for col in vector:
                table[c]+="<td bgcolor='" + coloredcolumns[col] +"' style='font-size:12px;padding:3px'>"+ col +"</td>"
                c=c+1
        table.reverse()
        html="<table class='table' ><tr>" + "</tr><tr>".join(table) + "</tr></table>"
        return html

        # show the alignment of multiple sentences as html table

    def mAlignmentToTableCode(self, arr, sentences):
        table = ["" for x in range(len(sentences))]  # reset Matrix Variable
        for vector in arr:
            coloredcolumns = self.coloring2(vector)
            c = 0
            for col in vector:
                table[c] += "<td bgcolor='" + coloredcolumns[col] + "' data-toggle='tooltip'  title='"+col+"' style='display: inline-block;width:8px;border-radius:1px; margin: 1px;padding:3px'></td>"
                c = c + 1
        table.reverse()
        html = "<center><table class='table' style='padding:1px;width:100%' ><tr>" + "</tr><tr>".join(table) + "</tr></table></center>"
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

    def alignmentToText(self,alignment, outputfile="test.html"):
        text=[[],[]]
        relations=dict()
        len1=len(alignment)
        for column in alignment:
            if column['relation'] not in relations:
                relations[column['relation']]=1
            else:
                relations[column['relation']] += 1
            text[0].append("<span class='"+column['relation']+"'> " + column['sentence1'] + " </span>")
            text[1].append("<span class='"+column['relation']+"'> " + column['sentence2'] + " </span>")
        html="Length: "+ str(len1)+" &nbsp;&nbsp;|| &nbsp;&nbsp;"
        for rel in relations:
            html+="<span class='"+rel+"'> " +rel+" ("+ str(relations[rel]) + ") </span> &nbsp;&nbsp;|| &nbsp;&nbsp;"
        html+="SIMILARITY: "+"{:10.4f}".format((len1 -relations['notAligned']-relations['Gap'])/len1)
        div="<div class='row'><div class='col-md-6'> PL private </div><div class='col-md-6'> Github version </div><div class='col-md-6'>"+" ".join(text[0])+"</div><div class='col-md-6'>"+" ".join(text[1])+"</div><div class='col-md-12'><br><br><center>"+html+"<center></div></div>"
        return div #[" ".join(text[0])," ".join(text[1])]