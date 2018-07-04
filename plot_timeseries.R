sentiment_timeseries = read.csv("sentiment_timeseries.csv")
sentiment_timeseries = subset(sentiment_timeseries, select = c("time", "polarity", "subjectivity"))
library(ggplot2)
ggplot(sentiment_timeseries, aes(x= polarity, y = subjectivity )) + geom_point()
ggplot(sentiment_timeseries, aes(x=as.numeric(rownames(sentiment_timeseries)), y = polarity) ) + geom_point()
ggplot(sentiment_timeseries, aes(x=as.numeric(rownames(sentiment_timeseries)), y = subjectivity) ) + geom_point()

write.csv(subset(sentiment_timeseries, select = c("polarity")), "polarity_timeseries_germex.csv", row.names = FALSE)
