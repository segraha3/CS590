
A <- c(1:3)
B <- c(4:6)

A
B

rbind(A,B)

mat <- matrix(1:9, nrow= 3)

mat

class(mat) == 'matrix'

mat2 <- matrix(1:25, nrow = 5, byrow = T)

mat2

mat2[2:3,2:3]

mat2[4:5,4:5]

sum(mat2)

help(runif)

matrix(runif(20, min = 1, max = 100), nrow=4)


