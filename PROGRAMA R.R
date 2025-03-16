install.packages('dplyr')
library(dplyr)

DataFrame = data.frame( areas= c(5,80,60,50,33,98), 
                        cultura = c(1,2,2,2,1,1),
                        litros = c(20,63,98,56,12,36))
                      
#media global de areas
media_litros_global = sum(DataFrame[,c('areas')])/length(DataFrame[,c('areas')])
print(media_litros_global)

#desvio global de areas
desvio_litros_global = sd(DataFrame[,c('areas')])
print(desvio_litros_global)

#media em m² de cada cultura
media_areas_culturas = DataFrame %>% group_by(cultura) %>% summarise(area_media = mean(areas))
print(media_areas_culturas)

#media de consumo em Litros de cada cultura
media_areas_culturas = DataFrame %>% group_by(cultura) %>% summarise(litros_media = mean(litros))
print(media_areas_culturas)

#desvio de consumo por cultura
desvio_litros_culturas = DataFrame %>% group_by(cultura) %>% summarise(consumo_medio = sd(litros))
print(desvio_litros_culturas)
