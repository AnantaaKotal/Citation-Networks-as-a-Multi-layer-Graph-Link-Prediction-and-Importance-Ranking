#!/usr/bin/python

import MySQLdb


db = MySQLdb.connect("localhost","root","Fish_7735","TESTDB" )

cursor = db.cursor()

sql = """insert into TESTDB.AUTHOR_AUTHOR
	select A.PAPER_ID, A.AUTHOR_ID, A.AUTHOR_NAME, C.AUTHOR_ID, C.AUTHOR_NAME
	from TESTDB.PAPER_AUTHOR as A 
	inner join
	(
	select PAPER_ID, count(*) as NBR_ATH from TESTDB.PAPER_AUTHOR
	GROUP BY PAPER_ID
	HAVING count(*) > 1
	) as B
	on A.PAPER_ID = B.PAPER_ID
	inner join TESTDB.PAPER_AUTHOR as C
	on A.PAPER_ID = C.PAPER_ID
	and A.AUTHOR_ID < C.AUTHOR_ID
	order by A.PAPER_ID asc, A.AUTHOR_ID asc, C.AUTHOR_ID asc"""
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()

db.close()
