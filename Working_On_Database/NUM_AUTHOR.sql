select PAPER_ID, count(*) as NBR_ATH from TESTDB.PAPER_AUTHOR
GROUP BY PAPER_ID
HAVING count(*) > 1 
order by 2 desc
