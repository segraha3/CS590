
#finishing up data frames from last week

#rbind and cbind to append rows and columns
c1 <- 1:10
c1

c2 <- letters[1:10]
c2

df <- data.frame(col.name1 = c1, col.name2 = c2)

df

df2 <- data.frame(col.name1 = 2000, col.name2 ='new')

df2

rbind(df, df2)

times.2 <- df$col.name1 *2
times.2

cbind(df, times.2)

peanut.weight <- data.frame(
    name = I(c('Bailey','Baily2','Wynne','Emery','Sullivan','Gregory')),
    weights = c(89,92,105,103,99,89)
)
peanut.skins <- data.frame(
    name = I(c('Bailey','Baily2','Wynne','Emery','Sullivan', 'brantley')),
    skins = c('Tan', 'Tan', 'pink', 'pink','tan','red')
)

peanut.weight

peanut.skins

#merge()
    #all.x - left 
    #all.y - right
    #all -outer
peanut <- merge(peanut.weight, peanut.skins, by.x='name', by.y ='name', all = T)

#any()
#is.na()

any(is.na(peanut))

any(is.na(peanut$skins))

peanut[is.na(peanut$skins),]

peanut[!is.na(peanut$weights),]

peanut$weights[is.na(peanut$weights)] <- mean(peanut$weights, na.rm =T)

peanut

#List

#vector
v <- c(1,2,3,4,5)

#matrix 
m <- matrix(1:10, nrow=2)

#df
df <- women

li <- list(v,m,df)

li

li <- list(sample_vec = v, sample_mat = m, sample_df = df)

li

li[1]

li['sample_vec']

li$sample_vec

li[['sample_vec']][1]

li[['sample_mat']][1,]

li[['sample_df']]['height']

double_list <- c(li,li)

double_list

str(double_list)

getwd()

setwd("C:/Users/gis/Desktop/CS590")

getwd()

#read.csv()

example <- read.csv('example.csv')

example

str(example)

colnames(example)

head(example)

read.table('example.csv', sep = ',', header = T)

library('data.table')

fread('example.csv')

df<- example
write.csv(df, 'output.csv')

library(readx1)


