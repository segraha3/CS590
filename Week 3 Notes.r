
#Matricies follow one datatype and have similar constraints as vectors
#Range of sequential numeric values
1:10

#Assign sequential numerica range to a vector
v <- 1:10
v

#matrix() functions
matrix(v)

matrix(v, nrow=2)

matrix(v, byrow=T, nrow=2)

matrix(1:12, byrow = T, nrow = 4)

Lewiston <- c(12,14,18,13,17)
Rocky.Mount <- c(11,19,21,15,18)
Whiteville <- c(14,17,23,11,9)

weights <- c(Lewiston, Rocky.Mount, Whiteville)

weights

weights.matrix <- matrix(weights, byrow = T, nrow = 3)

weights.matrix

#name row = rownames(), columns = colnames()
days <- c('M','T','W','Th','F')
loc.names <- c("Lewiston", "RockyMount", "Whiteille")

colnames(weights.matrix) <- days

rownames(weights.matrix) <- loc.names

weights.matrix

#a matrix with 5 rows and 10 columns
mat <-matrix(1:50, byrow = T, nrow=5)

mat

2*mat

mat/2

#the comparison operators (==, !=, >,<,>=,<=)
mat ^2

mat > 15

mat +mat

mat/mat

mat ^mat

mat2 <- matrix(1:9, nrow=3)

mat2*mat2 #multiply the elements

#%*%, matrix multiplication
mat2 %*% mat2

weights.matrix

colSums(weights.matrix)

rowSums(weights.matrix)

colMeans(weights.matrix)

rowMeans(weights.matrix)

#add the clayton location onto weights.matrix
Clayton <- c(17,23,15,19,13)


#cbind() or rbind()
ncsu.matrix <- rbind(weights.matrix, Clayton)

ncsu.matrix

Means.loc <- rowMeans(ncsu.matrix)

Means.loc

ncsu.matrix <- cbind(ncsu.matrix, Means.loc)

ncsu.matrix

short <- c(2,18,12)
long <- c(12, 11,10,9,8)

cbind(ncsu.matrix,short)

cbind(ncsu.matrix,long)

#example.matrix[row,col]
mat <-matrix(1:50, byrow =T, nrow = 5)

mat

mat[1,]

mat[,1]

mat[1:3,]

mat[1:2,1:3]

mat[,9:10]

#Factor and categorical matricies
#factor()

#Example: P(peanut), M(maize),S(soy), C(cotton)

crop <- c('P','P','C','M','C','S','P','S','M','P')
id <- c(1:10)

factor.crop <- factor(crop)

factor.crop

ord.cat <- c('Cold','Med','Hot')

#ordered = TRUE
#levels = c('The order')
temps <- c('cold','hot','hot','med','cold','hot','med')

fact.temps <- factor(temps, ordered = T, levels=c('cold', 'med', 'hot'))

fact.temps

#summary
summary(temps)

summary(fact.temps)


