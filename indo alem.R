install.packages("httr")
install.packages("jsonlite")

library(httr)
library(jsonlite)

cidade = URLencode("São Paulo")
pais = "BR"
api_key = "13ba7b34c4c1d8c96ee4d6fbb3292b5a"

url <- paste0("http://api.openweathermap.org/data/2.5/weather?q=", cidade, ",", pais, "&appid=", api_key, "&units=metric&lang=pt")
print(url)
response <- GET(url)
dados <- content(response, "parsed")

temperatura <- dados$main$temp
descricao <- dados$weather[[1]]$description

print(paste("Temperatura:", temperatura, "°C"))
print(paste("Condição:",descricao))
