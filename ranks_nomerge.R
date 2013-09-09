# Change the paths below for this to work!  There are three instances of
# /path/to which should be changed to your given path.

df <- read.csv('/path/to/AllLetters_proc.csv',stringsAsFactors=FALSE)

# we should fix the diacritics

# Goal: come up with an ambiguity metric
# first idea - weighted standard deviation within people and letters
library(SDMTools)
library(plyr)

wt.sd <- function (x, wt) 
{
  s = which(is.finite(x + wt))
  wt = wt[s]
  x = x[s]
  xbar = wt.mean(x, wt)
  return(sqrt(sum(wt * (x - xbar)^2 / (sum(wt)))))
}

sumsd <- ddply(df,.(id,rankname,sendername),summarize,
               wsd=wt.sd(rank,samples),
               num=length(rank),
               toprank=rank[order(samples,decreasing=T)][1],
               secondrank=rank[order(samples,decreasing=T)][2],
               thirdrank=rank[order(samples,decreasing=T)][3],
               fouthrank=rank[order(samples,decreasing=T)][4],               
               meanrank=wt.mean(rank,samples))
names(sumsd)[1] <- "letterid"
sumsd$id <- row.names(sumsd)
sumsd$wsd[is.na(sumsd$wsd)] <- 0

sumsd_sort <- sumsd[order(sumsd$wsd),]
sources<- subset(sumsd,rankname==sendername)[c('letterid','id')]
targets <- subset(sumsd,rankname!=sendername)[,c('letterid','id')]

letters <- merge(sources,targets,by='letterid')

letters <- rename(letters,c("id.x" = "source", "id.y" = "target"))

write.csv(letters,'/path/to/all_letter_edges.csv')
write.csv(sumsd,'/path/to/all_letter_nodes.csv')