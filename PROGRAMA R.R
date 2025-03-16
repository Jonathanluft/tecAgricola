install.packages('dplyr')
library(dplyr)

DataFrame = data.frame( areas= c(5,80,60,50,33,98), 
                        cultura = c(1,2,2,2,1,1),
                        litros = c(20,63,98,56,12,36))
                      

media_litros_global = sum(DataFrame[,c('areas')])/length(DataFrame[,c('areas')])
print(mediaitros_global)
desvio_litros_global = sd(DataFrame[,c('areas')])
print(desvio_litros_global)

dados_agrupados = DataFrame %>% group_by(cultura) %>% summarise(area_media = mean(areas))
print(dados_agrupados)


