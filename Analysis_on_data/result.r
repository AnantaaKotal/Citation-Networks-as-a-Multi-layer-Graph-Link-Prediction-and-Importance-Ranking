Call:
glm(formula = LINK ~ IN_DEGREE + OUT_DEGREE + AUTH_OVERLAP + 
    MAX_COLL + MEAN_COLL + MAX_CITE + MEAN_CITE + AvgCiteA + 
    AvgCiteB + AvgRefA + AvgRefB, family = "binomial", data = testdata)

Deviance Residuals: 
    Min       1Q   Median       3Q      Max  
-2.7620  -1.0683   0.5613   1.0164   1.3462  

Coefficients:
               Estimate Std. Error z value Pr(>|z|)    
(Intercept)  -3.848e-01  3.864e-03 -99.585  < 2e-16 ***
IN_DEGREE    -7.024e-05  1.366e-03  -0.051  0.95897    
OUT_DEGREE   -5.515e-06  1.341e-04  -0.041  0.96719    
AUTH_OVERLAP  1.337e+00  4.432e-01   3.016  0.00257 ** 
MAX_COLL      1.069e-01  1.885e-01   0.567  0.57046    
MEAN_COLL     1.352e-01  2.695e-01   0.502  0.61588    
MAX_CITE     -7.865e-03  8.022e-03  -0.980  0.32687    
MEAN_CITE     8.439e-03  2.171e-02   0.389  0.69748    
AvgCiteA     -9.537e-04  1.312e-05 -72.682  < 2e-16 ***
AvgCiteB      3.782e-07  1.328e-05   0.028  0.97728    
AvgRefA       7.963e-03  2.896e-05 274.949  < 2e-16 ***
AvgRefB      -8.488e-07  2.619e-05  -0.032  0.97415    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 1334289  on 1003001  degrees of freedom
Residual deviance: 1192042  on 1002990  degrees of freedom
AIC: 1192066

Number of Fisher Scoring iterations: 7

