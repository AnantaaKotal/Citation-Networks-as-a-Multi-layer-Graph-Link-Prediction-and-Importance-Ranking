#!/usr/bin/python

import MySQLdb


def do():
	db = MySQLdb.connect("localhost","root","Fish_7735","TESTDB" )
	cursor = db.cursor()
	cursor1 = db.cursor()
	sql = "SELECT * FROM TESTDB.AUTHOR"
	try:
		
		cursor.execute(sql)
 		
		results = cursor.fetchall()
   		
		for row in results:
			aname = row[0]
			aid = row[1]
      			
			updatesql="UPDATE PAPER_AUTHOR SET AUTHOR_ID=%d WHERE AUTHOR_NAME='%s'" % (aid, aname)
		
			cursor1.execute(updatesql)
			db.commit()			
	except:
		print "Error: unable to fecth data"

	
	db.close()

