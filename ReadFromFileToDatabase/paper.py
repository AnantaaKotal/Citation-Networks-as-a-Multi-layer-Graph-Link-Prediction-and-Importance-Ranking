#!/usr/bin/python

import re
import find_str

endOfLine='\n'
paper="Paper:"
title="Title:"

def GetPaper(line):
	line=line.replace(endOfLine,"").replace(paper,"")
	paperid=line.replace(" hep-th/","")
	return line, paperid

def GetTitle(line):
	line=line.replace(endOfLine,"").replace(title,"")
	return line

def GetAuthor(line):
		
		NameOfAuthors=[]
		line=re.sub(r'\([^)]*\)', '', line)
		line=line.replace(endOfLine,"").replace("Authors:","").replace("Author:","").replace(" and ",",")
		line=line.split(",")
		for name in line:
			name=re.sub('[^A-Za-z .]+', '', name)
			
			name=name.lstrip()
			
			name=name.replace(". ",".")
			
			if (name[0:1]=='('):	
				name=""
			
			try:
				index1=name.index('(')
				name=name[0:index1]
			except ValueError:
				name=name
			
			index=find_str.find_str(name," Department")
			if (index!=-1):
				i=index-1
				name=name[0:i]

			index=find_str.find_str(name," University")
			if (index!=-1):
				i=index-1
				name=name[0:i]

			index=find_str.find_str(name," Institute")
			if (index!=-1):
				i=index-1
				name=name[0:i]

			index=find_str.find_str(name," Academ")
			if (index!=-1):
				i=index-1
				name=name[0:i]
				

			if (name!=""):
				NameOfAuthors.append(name)
				

		return NameOfAuthors



	

