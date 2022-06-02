# Extensão de gelo no oceano ártico
Esse algoritmo usa redes neurais recorrentes para a previsão da extensão de gelo no oceano ártico. 
Os dados utilizados são disponibilizados no site https://nsidc.org/. 
O propósito do projeto é treinar habilidades no campo de machine learning. Uma inspiração para esse projeto foi a gráfico interativo presente no site https://nsidc.org/arcticseaicenews/charctic-interactive-sea-ice-graph/, além do tema ser relevante no contexto das mudanças climáticas. 

# Como funciona o projeto
No arquivo ftpdata.py é utilizado o protocolo ftp para extrair os arquivos necessários para a análise. É necessário alterar as variáveis "destdir" e "password" para realizar o download dos dados via FTP.
Será feito o download de três arquivos, apenas o arquivo "N_seaice_extent_daily_v3.0.csv" será utilizado. 
No arquivo "previsao_artico_um_previsor.py" é realizado o pré-processamento dos dados, eliminando dados desnecessários para o projeto.
Também nesse arquivo se encontra a estrutura da rede neural.
A variável "Qtd_dias_previsao" determina a quantidade em dias que a rede neural fará a previsão. 
Foi utilizada a classe EarlyStopping para parar o treinamento quando o mesmo não consegue de melhorar o desempenho.
Foram utilizadas quatro camadas mais a camada de saída na construção da rede neural, a função de ativação foi a "sigmoid" e a lossFunction utilizada foi a "mean_squared_error".

# Testes efetuados
Em um teste para o tempo de 90 dias foram obtidos os seguintes resultados:

Valor médio da previsão: 13.9089155

Valor médio real: 13.867099999999997

![Previsão_extensão_artico_90dias](https://user-images.githubusercontent.com/54844874/171716675-ba0c0fd9-b4ce-49b8-b45d-909d0ba5efcf.png)


# Mudanças e implementações futuras
Uma possibilidade de melhorar o projeto é utilizar mais de um atributo previsor. 
Nesse projeto, apenas foram utilizados os dados históricos da extensão de gelo no oceano ártico. 
Porém, utilizando os dados de CO2 na atmosfera e dos índices ENSO (El niño southern oscillation), pode-se obter dados mais robustos, mesmo em períodos mais longos de tempo de previsão, além de mostrar possíveis correlações entre esses atributos. 
