SELECT A.FromPaperID, A.ToPaperID, count(*) as AUTH_OVERLAP
From TESTDB.AUTHOR_CITE as A
inner join TESTDB.AUTHOR_CITE as B
ON A.NEW_AUTHOR_ID=B.OLD_AUTHOR_ID
group by A.FromPaperID, A.ToPaperID

limit 100
