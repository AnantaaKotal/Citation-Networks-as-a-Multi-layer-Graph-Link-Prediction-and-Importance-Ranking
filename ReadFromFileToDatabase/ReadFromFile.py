#!/usr/bin/python

import glob
import sys
import re
import paper
import insert

def do():
	DateList=[]
	i=0
	dirStr='/home/anantaa/data/'
	fileStr='/*.abs'
	print
	n=1992
	while (n<2004):	
		s=str(n)
		path=dirStr+s+fileStr
		endOfLine='\n'
		files=glob.glob(path)
		
		for file in files:
			f=open(file,'r')
			NameOfAuthors=[]
			r=0
			Trow=0
			arow=0
			for line in f:
				r=r+1
				if line.startswith("Paper:"):
					Paper,paperid=paper.GetPaper(line)
				if line.startswith("Date:"):
					DateList.append(line.replace(endOfLine,"").replace("Date:",""))
				if line.startswith("Title:"):
					Title=paper.GetTitle(line)
					Trow=r
				if r==Trow+1 and r!=1 and not line.startswith("Author"):
					line=line.replace(endOfLine,"")
					Title=Title+line.lstrip()
					Trow=r
				if line.startswith("Author"):
					arow=r
					authorline=line
				if r==arow+1 and r!=1 and not line.startswith("Comment"):
					line=line.replace(endOfLine,"")
					authorline=authorline+line.lstrip()
					arow=r
			NameOfAuthors=paper.GetAuthor(authorline)
			insert.insertIntoPaper(paperid,Paper,Title)	
			for name in NameOfAuthors:
				insert.insertIntoAuthor(name)
				insert.insertIntoPaperAuthor(name,Title,paperid)
			
			i=i+1
			f.close()
		n=n+1
	print "No. of Files Read: %d" %i
	print "Read From All Files"


