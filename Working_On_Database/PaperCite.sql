select FromPaperID, count(*) as NBR_PAPER_CITE from TESTDB.PaperCitation
GROUP BY FromPaperID
order by 2 desc
