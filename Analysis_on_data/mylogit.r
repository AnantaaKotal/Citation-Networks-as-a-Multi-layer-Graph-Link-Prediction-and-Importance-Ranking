con <- dbConnect(RMySQL::MySQL(), dbname = "TESTDB",username="root",password="Fish_7735")
st01 <- "SELECT * from TESTDB.FNL_PRM"
testdata <- dbGetQuery(con, st01)
mylogit <- glm(LINK ~ IN_DEGREE + OUT_DEGREE + AUTH_OVERLAP + MAX_COLL + MEAN_COLL + MAX_CITE + MEAN_CITE + AvgCiteA + AvgCiteB + AvgRefA + AvgRefB, data = testdata, family = "binomial")
summary(mylogit)
