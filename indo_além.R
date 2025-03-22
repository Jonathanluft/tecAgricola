#instalando bibliotecas necessarias
install.packages("httr")
install.packages("jsonlite")

#Chamando bibliotecas
library(httr)
library(jsonlite)

#Definindo localizcao
cidade = URLencode("São Paulo")
pais = "BR"
api_key = "13ba7b34c4c1d8c96ee4d6fbb3292b5a"

#construindo url de requisisao
url = paste0("http://api.openweathermap.org/data/2.5/weather?q=", cidade, ",", pais, "&appid=", api_key, "&units=metric&lang=pt")

#fazendo requisicao a api
response = GET(url)

#transformando json em lista para facilitar o acesso
dados = content(response, "parsed")

str(dados)
#acessando dadosda lista
temperatura = dados$main$temp
descricao = dados$weather[[1]]$description
temp_max = dados$main$temp_max
umidade = dados$main$humidity

#paste é usado para concatenar str e variaveis, semelante ao printf em py
print(paste("Temperatura:", temperatura, "°C"))
print(paste("Temperatura máxima:",temp_max, "C"))
print(paste("Umidade:",umidade))
print(paste("Condição:", descricao))
