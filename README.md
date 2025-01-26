# Dashboard COVID 19
 Dashboard COVID 19


# **Tópicos**

<ol type="1">
  <li>Introdução;</li>
  <li>Análise Exploratória de Dados;</li>
  <li>Visualização Interativa de Dados;</li>
  <li>Storytelling.</li>
</ol>


### **1.1. TLDR**

 - **Dashboard**:
  - Google Data Studio ([link](https://lookerstudio.google.com/reporting/9171005c-8a74-4c12-a66e-cbd1afd6eeef))
 - **Processamento**:
  - GitHub (`link`).
 - **Fontes**:
  - Casos pela universidade John Hopkins ([link](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports));
  - Vacinação pela universidade de Oxford ([link](https://covid.ourworldindata.org/data/owid-covid-data.csv)).


  ### **1.2. Pandemia Coronavírus 2019**

> A COVID-19 é uma infecção respiratória aguda causada pelo coronavírus SARS-CoV-2, potencialmente grave, de elevada transmissibilidade e de distribuição global. Fonte: Governo brasileiro ([link](https://www.gov.br/saude/pt-br/coronavirus/o-que-e-o-coronavirus)).


A disponibilidade de dados sobre a evolução da pandemia no tempo em uma determinada região geográfica é fundamental para o seu combate! Este projeto busca construir um dashboard de dados para exploração e visualização interativa de dados sobre o avanço de casos e da vacinação do Brasil. O processamento de dados está neste `link` e o dashboard, neste `link`.

### **1.3. Dados**

Os dados sobre **casos da COVID-19** são compilados pelo centro de ciência de sistemas e engenharia da universidade americana **John Hopkins** ([link](https://www.jhu.edu)). Os dados são atualizados diariamente deste janeiro de 2020 com uma granularidade temporal de dias e geográfica de regiões de países (estados, condados, etc.). O website do projeto pode ser acessado neste [link](https://systems.jhu.edu/research/public-health/ncov/) enquanto os dados, neste [link](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports). Abaixo estão descritos os dados derivados do seu processamento.

 - **date**: data de referência;
 - **state**: estado;
 - **country**: país;
 - **population**: população estimada;
 - **confirmed**: número acumulado de infectados;
 - **confirmed_1d**: número diário de infectados;
 - **confirmed_moving_avg_7d**: média móvel de 7 dias do número diário de infectados;
 - **confirmed_moving_avg_7d_rate_14d**: média móvel de 7 dias dividido pela média móvel de 7 dias de 14 dias atrás;
 - **deaths**: número acumulado de mortos;
 - **deaths_1d**: número diário de mortos;
 - **deaths_moving_avg_7d**: média móvel de 7 dias do número diário de mortos;
 - **deaths_moving_avg_7d**: média móvel de 7 dias dividido pela média móvel de 7 dias de 14 dias atrás;
 - **month**: mês de referência;
 - **year**: ano de referência.

 Os dados sobre **vacinação da COVID-19** são compilados pelo projeto Nosso Mundo em Dados (*Our World in Data* ou OWID) da universidade britânica de **Oxford** ([link](https://www.ox.ac.uk)). Os dados são **atualizados diariamente** deste janeiro de 2020 com uma **granularidade temporal de dias e geográfica de países**. O website do projeto pode ser acessado neste [link](https://ourworldindata.org) enquanto os dados, neste [link](https://covid.ourworldindata.org/data/owid-covid-data.csv). Abaixo estão descritos os dados derivados do seu processamento.


  - **date**: data de referência;
 - **country**: país;
 - **population**: população estimada;
 - **total**: número acumulado de doses administradas;
 - **one_shot**: número acumulado de pessoas com uma dose;
 - **one_shot_perc**: número acumulado relativo de pessoas com uma dose;
 - **two_shots**: número acumulado de pessoas com duas doses;
 - **two_shot_perc**: número acumulado relativo de pessoas com duas doses;
 - **three_shots**: número acumulado de pessoas com três doses;
 - **three_shot_perc**: número acumulado relativo de pessoas com três doses;
 - **month**: mês de referência;
 - **year**: ano de referência.



# Dados sobre Casos e Vacinação da COVID-19

## Contexto
A pandemia de COVID-19 trouxe desafios globais sem precedentes, destacando a importância de dados confiáveis para informar a tomada de decisão. Através da análise dos dados compilados pela Universidade John Hopkins, buscamos entender a dinâmica de casos, mortes e vacinações ao longo do tempo e em diferentes regiões geográficas.

## Objetivo
O objetivo principal desta análise é fornecer insights significativos sobre a evolução da pandemia e os avanços na vacinação, de forma a apoiar decisões baseadas em dados.

---

## Principais Insights

### 1. **Casos e Mortes nas últimas 24 horas**
- **Casos registrados:** A variação diária fornece um panorama imediato da disseminação do vírus.
- **Mortes registradas:** Este KPI destaca os impactos mais graves da pandemia e auxilia na avaliação de regiões mais afetadas.

### 2. **Média Móvel (7 dias)**
- A média móvel de casos e mortes ajuda a suavizar flutuações diárias e a identificar tendências consistentes.

### 3. **Tendência de Casos e Mortes**
- Análise de longo prazo revelou picos durante ondas de novas variantes e reduções após campanhas de vacinação bem-sucedidas.

### 4. **Distribuição Geográfica dos Casos**
- Identificamos regiões mais afetadas, destacando a necessidade de alocação direcionada de recursos.

### 5. **Vacinação**
- Proporção de vacinados com:
  - **1ª dose:** Indicativo do alcance inicial das campanhas.
  - **2ª dose:** Métrica de imunização completa.
  - **3ª dose:** Reflete a adesão às doses de reforço.

---

## Histórias dos Dados

### **A Expansão Global do Vírus**
- No início da pandemia, os casos se concentravam em poucas regiões, mas rapidamente se disseminaram. Análises temporais mostraram o impacto de medidas como lockdowns e uso de máscaras.

### **Ondas de Infecção**
- Ondas sucessivas de infecções coincidiram com o surgimento de novas variantes, sendo marcadas por aumentos abruptos nos indicadores de casos e mortes.

### **Impacto das Vacinas**
- Após o lançamento das vacinas, observou-se uma redução consistente na taxa de mortalidade e na gravidade dos casos em populações amplamente vacinadas.

### **Desigualdade Regional**
- Análises geográficas revelaram desigualdades no acesso à vacinação e no impacto da pandemia. Regiões menos desenvolvidas apresentaram taxas de mortalidade mais altas.

---

## Visualizações Relevantes

1. **Linha do Tempo da Pandemia**
   - Evolução dos casos e mortes.

2. **Mapas Geográficos**
   - Distribuição de casos e vacinas por região.

3. **Gráficos de Médias Móveis**
   - Comparativos de tendências entre períodos distintos.

---

## Conclusão
A análise demonstrou como a combinação de medidas preventivas e vacinação em larga escala foi determinante para mitigar os impactos da pandemia. Destacou ainda a importância de monitorar indicadores de saúde para gestão eficaz de crises futuras.


