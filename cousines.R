library(rjson)
library(parallel)
library(caret)

cl<-makeCluster(7)
setwd("~/Desktop/Kaggle/Cousine/")
traindta <- fromJSON(file = "train.json")
ingredients <- c()
itmnum <- c()
cousine <- c()

for (i in 1:length(traindta)){
  ingredients <- unique(append(ingredients,traindta[[i]][[3]]))
  itmnum <- append(itmnum,traindta[[i]][[1]])
  cousine <- append(cousine, traindta[[i]][[2]])
}

switches <- as.data.frame(t(parSapply(cl, traindta,filp <- function(point,ingredients) {
  out <- ingredients %in% point[[3]]
  out[out==TRUE]<-1
  return(out)
  },ingredients)))

names(switches) <- ingredients

switches[,"itmnum"]<- itmnum
switches[,"cousine"]<- cousine
switches[is.na]<-0

stopCluster(cl)

partit <- createDataPartition(y = switches$cousine,p = 0.8,list = FALSE,times = 1)

switches.lr <- glm.fit(switches[partit,1:(length(switches)-2)],switches[partit,length(switches)],family = "binomial")

switches.pca <- prcomp(switches[,0:6714]) 
corout <- cor(switches[partit,1:(length(switches)-2)])
