#!/usr/bin/python

import MySQLdb


def insertIntoPaper(paperid,Paper,Title):
	db = MySQLdb.connect("localhost","root","Fish_7735","TESTDB" )

	cursor = db.cursor()
	sql="INSERT INTO PAPER(PAPER_ID,PAPER_NO,TITLE)\
	VALUES('%s', '%s', '%s')"%(paperid,Paper,Title)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()

def insertIntoAuthor(name):
	db = MySQLdb.connect("localhost","root","Fish_7735","TESTDB" )

	cursor = db.cursor()
	sql="INSERT INTO AUTHOR(AUTHOR_NAME)\
	VALUES('%s')"%(name)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()

	db.close()



def insertIntoPaperAuthor(name,Title,paperid):
	db = MySQLdb.connect("localhost","root","Fish_7735","TESTDB" )

	cursor = db.cursor()
	sql="INSERT INTO PAPER_AUTHOR(AUTHOR_NAME,PAPER_NAME,PAPER_ID)\
	VALUES('%s', '%s', '%s')"%(name,Title,paperid)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()

	db.close()



