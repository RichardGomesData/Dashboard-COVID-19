{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KJqp9AANOCtf"
      },
      "source": [
        "\n",
        "#  Análise de Dados: COVID-19 Dashboard\n",
        "\n",
        "\n",
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "d9jDtUbDOE1-"
      },
      "source": [
        "# **Tópicos**\n",
        "\n",
        "<ol type=\"1\">\n",
        "  <li>Introdução;</li>\n",
        "  <li>Análise Exploratória de Dados;</li>\n",
        "  <li>Visualização Interativa de Dados;</li>\n",
        "  <li>Storytelling.</li>\n",
        "</ol>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SmoHgt-lwkpD"
      },
      "source": [
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GABI6OW8OfQ2"
      },
      "source": [
        "# **Aulas**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "muD1vxozykSC"
      },
      "source": [
        "## 1\\. Introdução"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MHESfVrl-rPV"
      },
      "source": [
        "### **1.1. TLDR**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Kbt89uW55ynj"
      },
      "source": [
        " - **Dashboard**:\n",
        "  - Google Data Studio ([link](https://lookerstudio.google.com/reporting/9171005c-8a74-4c12-a66e-cbd1afd6eeef))\n",
        " - **Processamento**:\n",
        "  - GitHub (`link`).\n",
        " - **Fontes**:\n",
        "  - Casos pela universidade John Hopkins ([link](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports));\n",
        "  - Vacinação pela universidade de Oxford ([link](https://covid.ourworldindata.org/data/owid-covid-data.csv))."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uBq6aQxeB4r0"
      },
      "source": [
        "### **1.2. Pandemia Coronavírus 2019**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "caKO04G0tzxc"
      },
      "source": [
        "> A COVID-19 é uma infecção respiratória aguda causada pelo coronavírus SARS-CoV-2, potencialmente grave, de elevada transmissibilidade e de distribuição global. Fonte: Governo brasileiro ([link](https://www.gov.br/saude/pt-br/coronavirus/o-que-e-o-coronavirus))."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UrsxlQhH7WrD"
      },
      "source": [
        "A disponibilidade de dados sobre a evolução da pandemia no tempo em uma determinada região geográfica é fundamental para o seu combate! Este projeto busca construir um dashboard de dados para exploração e visualização interativa de dados sobre o avanço de casos e da vacinação do Brasil. O processamento de dados está neste `link` e o dashboard, neste `link`."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oo-6n3_GH0CT"
      },
      "source": [
        "### **1.3. Dados**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "q9Kj_d3c3Hmd"
      },
      "source": [
        "Os dados sobre **casos da COVID-19** são compilados pelo centro de ciência de sistemas e engenharia da universidade americana **John Hopkins** ([link](https://www.jhu.edu)). Os dados são atualizados diariamente deste janeiro de 2020 com uma granularidade temporal de dias e geográfica de regiões de países (estados, condados, etc.). O website do projeto pode ser acessado neste [link](https://systems.jhu.edu/research/public-health/ncov/) enquanto os dados, neste [link](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports). Abaixo estão descritos os dados derivados do seu processamento."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7hKS37TRwvG7"
      },
      "source": [
        " - **date**: data de referência;\n",
        " - **state**: estado;\n",
        " - **country**: país;\n",
        " - **population**: população estimada;\n",
        " - **confirmed**: número acumulado de infectados;\n",
        " - **confirmed_1d**: número diário de infectados;\n",
        " - **confirmed_moving_avg_7d**: média móvel de 7 dias do número diário de infectados;\n",
        " - **confirmed_moving_avg_7d_rate_14d**: média móvel de 7 dias dividido pela média móvel de 7 dias de 14 dias atrás;\n",
        " - **deaths**: número acumulado de mortos;\n",
        " - **deaths_1d**: número diário de mortos;\n",
        " - **deaths_moving_avg_7d**: média móvel de 7 dias do número diário de mortos;\n",
        " - **deaths_moving_avg_7d**: média móvel de 7 dias dividido pela média móvel de 7 dias de 14 dias atrás;\n",
        " - **month**: mês de referência;\n",
        " - **year**: ano de referência."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Io6Yn0Yi7woI"
      },
      "source": [
        "Os dados sobre **vacinação da COVID-19** são compilados pelo projeto Nosso Mundo em Dados (*Our World in Data* ou OWID) da universidade britânica de **Oxford** ([link](https://www.ox.ac.uk)). Os dados são **atualizados diariamente** deste janeiro de 2020 com uma **granularidade temporal de dias e geográfica de países**. O website do projeto pode ser acessado neste [link](https://ourworldindata.org) enquanto os dados, neste [link](https://covid.ourworldindata.org/data/owid-covid-data.csv). Abaixo estão descritos os dados derivados do seu processamento."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oF5oDfm07woK"
      },
      "source": [
        " - **date**: data de referência;\n",
        " - **country**: país;\n",
        " - **population**: população estimada;\n",
        " - **total**: número acumulado de doses administradas;\n",
        " - **one_shot**: número acumulado de pessoas com uma dose;\n",
        " - **one_shot_perc**: número acumulado relativo de pessoas com uma dose;\n",
        " - **two_shots**: número acumulado de pessoas com duas doses;\n",
        " - **two_shot_perc**: número acumulado relativo de pessoas com duas doses;\n",
        " - **three_shots**: número acumulado de pessoas com três doses;\n",
        " - **three_shot_perc**: número acumulado relativo de pessoas com três doses;\n",
        " - **month**: mês de referência;\n",
        " - **year**: ano de referência."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EkVv4SCzIrxS"
      },
      "source": [
        "## 2\\. Análise Exploratória de Dados"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5qb_q_g0W1xq"
      },
      "source": [
        "Nesta sessão vamos utilizar os seguintes pacotes Python para processar os dados bruto em um formato adequado para um painel para exploração interativa de dados."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "1X3WC_QYUlAz"
      },
      "outputs": [],
      "source": [
        "import math\n",
        "from typing import Iterator\n",
        "from datetime import datetime, timedelta\n",
        "\n",
        "import numpy as np\n",
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aP2Dlk9kOqCf"
      },
      "source": [
        "### **2.1. Casos**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8L5p6NGWaeSi"
      },
      "source": [
        "Vamos processar os dados de **casos** da universidade John Hopkins.\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Nd159jDC8Dm-"
      },
      "source": [
        "#### **2.1.1. Extração**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QvRDLv8xVm7Y"
      },
      "source": [
        "O dado está compilado em um arquivo por dia, exemplo para 2021/12/01."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "GmsdWZKzKWup"
      },
      "outputs": [],
      "source": [
        "cases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-12-2021.csv', sep=',')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "bHg1MA4AKaeC",
        "outputId": "5cbf06db-da4e-4c1f-b764-bae80c382a7f"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>FIPS</th>\n",
              "      <th>Admin2</th>\n",
              "      <th>Province_State</th>\n",
              "      <th>Country_Region</th>\n",
              "      <th>Last_Update</th>\n",
              "      <th>Lat</th>\n",
              "      <th>Long_</th>\n",
              "      <th>Confirmed</th>\n",
              "      <th>Deaths</th>\n",
              "      <th>Recovered</th>\n",
              "      <th>Active</th>\n",
              "      <th>Combined_Key</th>\n",
              "      <th>Incident_Rate</th>\n",
              "      <th>Case_Fatality_Ratio</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>2021-01-13 05:22:15</td>\n",
              "      <td>33.93911</td>\n",
              "      <td>67.709953</td>\n",
              "      <td>53584</td>\n",
              "      <td>2301</td>\n",
              "      <td>44608</td>\n",
              "      <td>6675</td>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>137.647787</td>\n",
              "      <td>4.294192</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Albania</td>\n",
              "      <td>2021-01-13 05:22:15</td>\n",
              "      <td>41.15330</td>\n",
              "      <td>20.168300</td>\n",
              "      <td>64627</td>\n",
              "      <td>1252</td>\n",
              "      <td>38421</td>\n",
              "      <td>24954</td>\n",
              "      <td>Albania</td>\n",
              "      <td>2245.708527</td>\n",
              "      <td>1.937271</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Algeria</td>\n",
              "      <td>2021-01-13 05:22:15</td>\n",
              "      <td>28.03390</td>\n",
              "      <td>1.659600</td>\n",
              "      <td>102641</td>\n",
              "      <td>2816</td>\n",
              "      <td>69608</td>\n",
              "      <td>30217</td>\n",
              "      <td>Algeria</td>\n",
              "      <td>234.067409</td>\n",
              "      <td>2.743543</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Andorra</td>\n",
              "      <td>2021-01-13 05:22:15</td>\n",
              "      <td>42.50630</td>\n",
              "      <td>1.521800</td>\n",
              "      <td>8682</td>\n",
              "      <td>86</td>\n",
              "      <td>7930</td>\n",
              "      <td>666</td>\n",
              "      <td>Andorra</td>\n",
              "      <td>11236.653077</td>\n",
              "      <td>0.990555</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Angola</td>\n",
              "      <td>2021-01-13 05:22:15</td>\n",
              "      <td>-11.20270</td>\n",
              "      <td>17.873900</td>\n",
              "      <td>18343</td>\n",
              "      <td>422</td>\n",
              "      <td>15512</td>\n",
              "      <td>2409</td>\n",
              "      <td>Angola</td>\n",
              "      <td>55.811022</td>\n",
              "      <td>2.300605</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   FIPS Admin2 Province_State Country_Region          Last_Update       Lat  \\\n",
              "0   NaN    NaN            NaN    Afghanistan  2021-01-13 05:22:15  33.93911   \n",
              "1   NaN    NaN            NaN        Albania  2021-01-13 05:22:15  41.15330   \n",
              "2   NaN    NaN            NaN        Algeria  2021-01-13 05:22:15  28.03390   \n",
              "3   NaN    NaN            NaN        Andorra  2021-01-13 05:22:15  42.50630   \n",
              "4   NaN    NaN            NaN         Angola  2021-01-13 05:22:15 -11.20270   \n",
              "\n",
              "       Long_  Confirmed  Deaths  Recovered  Active Combined_Key  \\\n",
              "0  67.709953      53584    2301      44608    6675  Afghanistan   \n",
              "1  20.168300      64627    1252      38421   24954      Albania   \n",
              "2   1.659600     102641    2816      69608   30217      Algeria   \n",
              "3   1.521800       8682      86       7930     666      Andorra   \n",
              "4  17.873900      18343     422      15512    2409       Angola   \n",
              "\n",
              "   Incident_Rate  Case_Fatality_Ratio  \n",
              "0     137.647787             4.294192  \n",
              "1    2245.708527             1.937271  \n",
              "2     234.067409             2.743543  \n",
              "3   11236.653077             0.990555  \n",
              "4      55.811022             2.300605  "
            ]
          },
          "execution_count": 3,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "cases.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XoGYHPcoKXSV"
      },
      "source": [
        "Portanto, precisaremos iterar dentro de um intervalo de tempo definido para extraí-lo."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "yvNNHQWjF1LI"
      },
      "outputs": [],
      "source": [
        "def date_range(start_date: datetime, end_date: datetime) -> Iterator[datetime]:\n",
        "  date_range_days: int = (end_date - start_date).days\n",
        "  for lag in range(date_range_days):\n",
        "    yield start_date + timedelta(lag)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "pUnc9yv5ISm1"
      },
      "outputs": [],
      "source": [
        "start_date = datetime(2021,  1,  1)\n",
        "end_date   = datetime(2021, 12, 31)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EqAuJfCkWKiz"
      },
      "source": [
        "De maneira iterativa, vamos selecionar as colunas de interesse e as linhas referentes ao Brasil."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Cbsd2j3ow01E"
      },
      "source": [
        "---\n",
        "Observação:\n",
        "na aula, o professor utiliza o método `append()`, mas esse método foi removido da\n",
        "biblioteca Pandas (foi descontinuado desde a versão 1.4 e removido a partir da versão 2.0). [Link da documentação para mais informações](https://pandas.pydata.org/pandas-docs/version/1.5/whatsnew/v1.4.0.html#whatsnew-140-deprecations-frame-series-append)\n",
        "\n",
        "Seguindo a sintaxe recomendada pela documentação, segue abaixo o código atualizado utilizando `concat()`. [Link da documentação: pandas.concat()](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)\n",
        "\n",
        "---\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "Oxn7mkcc2pHR"
      },
      "outputs": [],
      "source": [
        "cases = None\n",
        "cases_is_empty = True\n",
        "\n",
        "for date in date_range(start_date=start_date, end_date=end_date):\n",
        "\n",
        "  date_str = date.strftime('%m-%d-%Y')\n",
        "  data_source_url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date_str}.csv'\n",
        "\n",
        "  case = pd.read_csv(data_source_url, sep=',')\n",
        "\n",
        "  case = case.drop(['FIPS', 'Admin2', 'Last_Update', 'Lat', 'Long_', 'Recovered', 'Active', 'Combined_Key', 'Case_Fatality_Ratio'], axis=1)\n",
        "  case = case.query('Country_Region == \"Brazil\"').reset_index(drop=True)\n",
        "  case['Date'] = pd.to_datetime(date.strftime('%Y-%m-%d'))\n",
        "  if cases_is_empty:\n",
        "    cases = case\n",
        "    cases_is_empty = False\n",
        "  else:\n",
        "    cases = pd.concat([cases, case], axis= 0, ignore_index=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "nOYxy_zMKBin",
        "outputId": "3554c18b-4130-4e9a-a837-9df39ef35017"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Province_State</th>\n",
              "      <th>Country_Region</th>\n",
              "      <th>Confirmed</th>\n",
              "      <th>Deaths</th>\n",
              "      <th>Incident_Rate</th>\n",
              "      <th>Date</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>24</th>\n",
              "      <td>Sao Paulo</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>1466191</td>\n",
              "      <td>46775</td>\n",
              "      <td>3192.990778</td>\n",
              "      <td>2021-01-01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>51</th>\n",
              "      <td>Sao Paulo</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>1467953</td>\n",
              "      <td>46808</td>\n",
              "      <td>3196.827966</td>\n",
              "      <td>2021-01-02</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>78</th>\n",
              "      <td>Sao Paulo</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>1471422</td>\n",
              "      <td>46845</td>\n",
              "      <td>3204.382565</td>\n",
              "      <td>2021-01-03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>105</th>\n",
              "      <td>Sao Paulo</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>1473670</td>\n",
              "      <td>46888</td>\n",
              "      <td>3209.278136</td>\n",
              "      <td>2021-01-04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>132</th>\n",
              "      <td>Sao Paulo</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>1486551</td>\n",
              "      <td>47222</td>\n",
              "      <td>3237.329676</td>\n",
              "      <td>2021-01-05</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Province_State Country_Region  Confirmed  Deaths  Incident_Rate       Date\n",
              "24       Sao Paulo         Brazil    1466191   46775    3192.990778 2021-01-01\n",
              "51       Sao Paulo         Brazil    1467953   46808    3196.827966 2021-01-02\n",
              "78       Sao Paulo         Brazil    1471422   46845    3204.382565 2021-01-03\n",
              "105      Sao Paulo         Brazil    1473670   46888    3209.278136 2021-01-04\n",
              "132      Sao Paulo         Brazil    1486551   47222    3237.329676 2021-01-05"
            ]
          },
          "execution_count": 7,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "cases.query('Province_State == \"Sao Paulo\"').head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Z3HiqQRkOMGc"
      },
      "source": [
        "#### **2.1.2. Wrangling**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ceDNL40JzB0K"
      },
      "source": [
        "Vamos manipular os dados para o dashboard. O foco é em garantir uma boa granularidade e qualidade da base de dados."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "G66lP6tOqya_",
        "outputId": "5d010b15-bc3e-44ac-951a-808e5ec934fa"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "summary": "{\n  \"name\": \"cases\",\n  \"rows\": 9828,\n  \"fields\": [\n    {\n      \"column\": \"Province_State\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 27,\n        \"samples\": [\n          \"Goias\",\n          \"Para\",\n          \"Maranhao\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Country_Region\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 1,\n        \"samples\": [\n          \"Brazil\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Confirmed\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 717464,\n        \"min\": 41689,\n        \"max\": 4455011,\n        \"num_unique_values\": 9510,\n        \"samples\": [\n          199070\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Deaths\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 24220,\n        \"min\": 787,\n        \"max\": 155186,\n        \"num_unique_values\": 7807,\n        \"samples\": [\n          16136\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Incident_Rate\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3954.4200243768505,\n        \"min\": 2333.2776328647133,\n        \"max\": 21261.355551116696,\n        \"num_unique_values\": 9387,\n        \"samples\": [\n          6007.778295367166\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Date\",\n      \"properties\": {\n        \"dtype\": \"date\",\n        \"min\": \"2021-01-01 00:00:00\",\n        \"max\": \"2021-12-30 00:00:00\",\n        \"num_unique_values\": 364,\n        \"samples\": [\n          \"2021-07-13 00:00:00\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}",
              "type": "dataframe",
              "variable_name": "cases"
            },
            "text/html": [
              "\n",
              "  <div id=\"df-69ee9061-3872-4b80-ba9c-947b0dfb853e\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Province_State</th>\n",
              "      <th>Country_Region</th>\n",
              "      <th>Confirmed</th>\n",
              "      <th>Deaths</th>\n",
              "      <th>Incident_Rate</th>\n",
              "      <th>Date</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Acre</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>41689</td>\n",
              "      <td>796</td>\n",
              "      <td>4726.992352</td>\n",
              "      <td>2021-01-01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Alagoas</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>105091</td>\n",
              "      <td>2496</td>\n",
              "      <td>3148.928928</td>\n",
              "      <td>2021-01-01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Amapa</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>68361</td>\n",
              "      <td>926</td>\n",
              "      <td>8083.066602</td>\n",
              "      <td>2021-01-01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Amazonas</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>201574</td>\n",
              "      <td>5295</td>\n",
              "      <td>4863.536793</td>\n",
              "      <td>2021-01-01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Bahia</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>494684</td>\n",
              "      <td>9159</td>\n",
              "      <td>3326.039611</td>\n",
              "      <td>2021-01-01</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-69ee9061-3872-4b80-ba9c-947b0dfb853e')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-69ee9061-3872-4b80-ba9c-947b0dfb853e button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-69ee9061-3872-4b80-ba9c-947b0dfb853e');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-38345943-11e8-4bbd-af2c-8effb7640446\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-38345943-11e8-4bbd-af2c-8effb7640446')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-38345943-11e8-4bbd-af2c-8effb7640446 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "text/plain": [
              "  Province_State Country_Region  Confirmed  Deaths  Incident_Rate       Date\n",
              "0           Acre         Brazil      41689     796    4726.992352 2021-01-01\n",
              "1        Alagoas         Brazil     105091    2496    3148.928928 2021-01-01\n",
              "2          Amapa         Brazil      68361     926    8083.066602 2021-01-01\n",
              "3       Amazonas         Brazil     201574    5295    4863.536793 2021-01-01\n",
              "4          Bahia         Brazil     494684    9159    3326.039611 2021-01-01"
            ]
          },
          "execution_count": 9,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "cases.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z4yQeP4bVCC5",
        "outputId": "83b37e29-1f01-40f3-8ddf-416b2bf3c94b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(9828, 6)"
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "cases.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pRs8xDlcU-y0",
        "outputId": "67db10e6-f1d2-4fb4-d7bc-07f8a6517247"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 9828 entries, 0 to 9827\n",
            "Data columns (total 6 columns):\n",
            " #   Column          Non-Null Count  Dtype         \n",
            "---  ------          --------------  -----         \n",
            " 0   Province_State  9828 non-null   object        \n",
            " 1   Country_Region  9828 non-null   object        \n",
            " 2   Confirmed       9828 non-null   int64         \n",
            " 3   Deaths          9828 non-null   int64         \n",
            " 4   Incident_Rate   9828 non-null   float64       \n",
            " 5   Date            9828 non-null   datetime64[ns]\n",
            "dtypes: datetime64[ns](1), float64(1), int64(2), object(2)\n",
            "memory usage: 460.8+ KB\n"
          ]
        }
      ],
      "source": [
        "cases.info()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hgFFhUQgzFZ8"
      },
      "source": [
        "Começamos com o nome das colunas."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "1w9pQ8d_UCJO"
      },
      "outputs": [],
      "source": [
        "cases = cases.rename(\n",
        "  columns={\n",
        "    'Province_State': 'state',\n",
        "    'Country_Region': 'country'\n",
        "  }\n",
        ")\n",
        "\n",
        "for col in cases.columns:\n",
        "  cases = cases.rename(columns={col: col.lower()})"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "q2p4qjZUn-e2"
      },
      "source": [
        "Ajustamos o nome dos estados."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "id": "LBajRRZEnlms"
      },
      "outputs": [],
      "source": [
        "states_map = {\n",
        "    'Amapa': 'Amapá',\n",
        "    'Ceara': 'Ceará',\n",
        "    'Espirito Santo': 'Espírito Santo',\n",
        "    'Goias': 'Goiás',\n",
        "    'Para': 'Pará',\n",
        "    'Paraiba': 'Paraíba',\n",
        "    'Parana': 'Paraná',\n",
        "    'Piaui': 'Piauí',\n",
        "    'Rondonia': 'Rondônia',\n",
        "    'Sao Paulo': 'São Paulo'\n",
        "}\n",
        "\n",
        "cases['state'] = cases['state'].apply(lambda state: states_map.get(state) if state in states_map.keys() else state)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "niRCU0-JzHV2"
      },
      "source": [
        "Vamos então computar novas colunas para enriquecer a base de dados."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "V8Ijno5d28L-"
      },
      "source": [
        " - Chaves temporais:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "uRYhqYtRYYPI"
      },
      "outputs": [],
      "source": [
        "cases['month'] = cases['date'].apply(lambda date: date.strftime('%Y-%m'))\n",
        "cases['year']  = cases['date'].apply(lambda date: date.strftime('%Y'))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "d9tjVG7o2_IT"
      },
      "source": [
        " - População estimada do estado:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "id": "1U6wV_zngbZW"
      },
      "outputs": [],
      "source": [
        "cases['population'] = round(100000 * (cases['confirmed'] / cases['incident_rate']))\n",
        "cases = cases.drop('incident_rate', axis=1)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LCxMEJP53E3v"
      },
      "source": [
        " - Número, média móvel (7 dias) e estabilidade (14 dias) de casos e mortes por estado:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZSHsw4H1oyjI"
      },
      "source": [
        "| 1 | 2 | 3 | 4 | 5 | 6 | <font color='red'>7</font> | <font color='green'>8</font> | 9 | 10 | 11 | 12 | 13 | <font color='blue'>14<font color='red'> | 15 | 16 | 17 | 18 | 19 | 20 | 21 |\n",
        "| - | - | - | - | - | - | - | - | - | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |\n",
        "| <font color='red'>D-6</font> | <font color='red'>D-5</font> | <font color='red'>D-4</font> | <font color='red'>D-3</font> | <font color='red'>D-2</font> | <font color='red'>D-1</font> | <font color='red'>D0</font> | | | | | | | | | | | | | | |\n",
        "| D-7 | <font color='green'>D-6</font> | <font color='green'>D-5</font> | <font color='green'>D-4</font> | <font color='green'>D-3</font> | <font color='green'>D-2</font> | <font color='green'>D-1</font> | <font color='green'>D0</font> | | | | | | | | | | | | | |\n",
        "| D-13 | D-12 | D-11 | D-10 | D-9 | D-8 | D-7 | <font color='blue'>D-6</font> | <font color='blue'>D-5</font> | <font color='blue'>D-4</font> | <font color='blue'>D-3</font> | <font color='blue'>D-2</font> | <font color='blue'>D-1</font> | <font color='blue'>D0</font> | | | | | | | |"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Mbmf8xcn0cmy"
      },
      "source": [
        "\n",
        "\n",
        "---\n",
        "Observação: como explicado anteriormente, o código revisado utilizando `concat()` está apresentado abaixo.\n",
        "\n",
        "\n",
        "---\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "id": "ow_uWrO1gTGT"
      },
      "outputs": [],
      "source": [
        "cases_ = None\n",
        "cases_is_empty = True\n",
        "\n",
        "def get_trend(rate: float) -> str:\n",
        "\n",
        "  if np.isnan(rate):\n",
        "    return np.NaN\n",
        "\n",
        "  if rate < 0.75:    # Se a divisão for menor que 0.75 (correção 0.85)\n",
        "    status = 'downward'\n",
        "  elif rate > 1.15:\n",
        "    status = 'upward'\n",
        "  else:\n",
        "    status = 'stable'\n",
        "\n",
        "  return status\n",
        "\n",
        "\n",
        "for state in cases['state'].drop_duplicates():\n",
        "\n",
        "  cases_per_state = cases.query(f'state == \"{state}\"').reset_index(drop=True)\n",
        "  cases_per_state = cases_per_state.sort_values(by=['date'])\n",
        "\n",
        "  cases_per_state['confirmed_1d'] = cases_per_state['confirmed'].diff(periods=1)\n",
        "  cases_per_state['confirmed_moving_avg_7d'] = np.ceil(cases_per_state['confirmed_1d'].rolling(window=7).mean())\n",
        "  cases_per_state['confirmed_moving_avg_7d_rate_14d'] = cases_per_state['confirmed_moving_avg_7d']/cases_per_state['confirmed_moving_avg_7d'].shift(periods=14)\n",
        "  cases_per_state['confirmed_trend'] = cases_per_state['confirmed_moving_avg_7d_rate_14d'].apply(get_trend)\n",
        "\n",
        "  cases_per_state['deaths_1d'] = cases_per_state['deaths'].diff(periods=1)\n",
        "  cases_per_state['deaths_moving_avg_7d'] = np.ceil(cases_per_state['deaths_1d'].rolling(window=7).mean())\n",
        "  cases_per_state['deaths_moving_avg_7d_rate_14d'] = cases_per_state['deaths_moving_avg_7d']/cases_per_state['deaths_moving_avg_7d'].shift(periods=14)\n",
        "  cases_per_state['deaths_trend'] = cases_per_state['deaths_moving_avg_7d_rate_14d'].apply(get_trend)\n",
        "\n",
        "  if cases_is_empty:\n",
        "    cases_ = cases_per_state\n",
        "    cases_is_empty = False\n",
        "  else:\n",
        "    cases_ = pd.concat([cases_, cases_per_state],axis=0, ignore_index=True)\n",
        "\n",
        "cases = cases_\n",
        "cases_ = None"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hisru_0i07Pg"
      },
      "source": [
        "Garantir o tipo do dado é fundamental para consistência da base de dados. Vamos fazer o *type casting* das colunas."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "p7nalDg6KvFZ"
      },
      "outputs": [],
      "source": [
        "cases['population'] = cases['population'].astype('Int64')\n",
        "cases['confirmed_1d'] = cases['confirmed_1d'].astype('Int64')\n",
        "cases['confirmed_moving_avg_7d'] = cases['confirmed_moving_avg_7d'].astype('Int64')\n",
        "cases['deaths_1d'] = cases['deaths_1d'].astype('Int64')\n",
        "cases['deaths_moving_avg_7d'] = cases['deaths_moving_avg_7d'].astype('Int64')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LOwQaxtfgYka"
      },
      "source": [
        "Por fim, vamos reorganizar as colunas e conferir o resultado final."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "id": "6fkkdIXVZL-E"
      },
      "outputs": [],
      "source": [
        "cases = cases[['date', 'country', 'state', 'population', 'confirmed', 'confirmed_1d', 'confirmed_moving_avg_7d', 'confirmed_moving_avg_7d_rate_14d', 'confirmed_trend', 'deaths', 'deaths_1d', 'deaths_moving_avg_7d', 'deaths_moving_avg_7d_rate_14d', 'deaths_trend', 'month', 'year']]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "wUZetbA5zNO8",
        "outputId": "c6cc44ac-51e3-4ee5-a53c-7091d083b9d4"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>date</th>\n",
              "      <th>country</th>\n",
              "      <th>state</th>\n",
              "      <th>population</th>\n",
              "      <th>confirmed</th>\n",
              "      <th>confirmed_1d</th>\n",
              "      <th>confirmed_moving_avg_7d</th>\n",
              "      <th>confirmed_moving_avg_7d_rate_14d</th>\n",
              "      <th>confirmed_trend</th>\n",
              "      <th>deaths</th>\n",
              "      <th>deaths_1d</th>\n",
              "      <th>deaths_moving_avg_7d</th>\n",
              "      <th>deaths_moving_avg_7d_rate_14d</th>\n",
              "      <th>deaths_trend</th>\n",
              "      <th>month</th>\n",
              "      <th>year</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2021-01-01</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>41689</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>796</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2021-01-02</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>41941</td>\n",
              "      <td>252</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>798</td>\n",
              "      <td>2</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2021-01-03</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>42046</td>\n",
              "      <td>105</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>802</td>\n",
              "      <td>4</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2021-01-04</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>42117</td>\n",
              "      <td>71</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>806</td>\n",
              "      <td>4</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2021-01-05</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>42170</td>\n",
              "      <td>53</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>808</td>\n",
              "      <td>2</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>2021-01-06</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>42378</td>\n",
              "      <td>208</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>814</td>\n",
              "      <td>6</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>2021-01-07</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>42478</td>\n",
              "      <td>100</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>821</td>\n",
              "      <td>7</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>2021-01-08</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>42814</td>\n",
              "      <td>336</td>\n",
              "      <td>161</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>823</td>\n",
              "      <td>2</td>\n",
              "      <td>4</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>2021-01-09</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>42908</td>\n",
              "      <td>94</td>\n",
              "      <td>139</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>823</td>\n",
              "      <td>0</td>\n",
              "      <td>4</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>2021-01-10</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>43127</td>\n",
              "      <td>219</td>\n",
              "      <td>155</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>825</td>\n",
              "      <td>2</td>\n",
              "      <td>4</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>2021-01-11</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>43346</td>\n",
              "      <td>219</td>\n",
              "      <td>176</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>826</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>2021-01-12</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>43432</td>\n",
              "      <td>86</td>\n",
              "      <td>181</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>827</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>2021-01-13</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>43785</td>\n",
              "      <td>353</td>\n",
              "      <td>201</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>829</td>\n",
              "      <td>2</td>\n",
              "      <td>3</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>2021-01-14</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>44068</td>\n",
              "      <td>283</td>\n",
              "      <td>228</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>832</td>\n",
              "      <td>3</td>\n",
              "      <td>2</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>2021-01-15</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>44156</td>\n",
              "      <td>88</td>\n",
              "      <td>192</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>835</td>\n",
              "      <td>3</td>\n",
              "      <td>2</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>2021-01-16</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>44621</td>\n",
              "      <td>465</td>\n",
              "      <td>245</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>835</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>2021-01-17</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>44767</td>\n",
              "      <td>146</td>\n",
              "      <td>235</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>836</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>2021-01-18</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>44775</td>\n",
              "      <td>8</td>\n",
              "      <td>205</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>837</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18</th>\n",
              "      <td>2021-01-19</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>45208</td>\n",
              "      <td>433</td>\n",
              "      <td>254</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>839</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>2021-01-20</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>45429</td>\n",
              "      <td>221</td>\n",
              "      <td>235</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>840</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>20</th>\n",
              "      <td>2021-01-21</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>45729</td>\n",
              "      <td>300</td>\n",
              "      <td>238</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>844</td>\n",
              "      <td>4</td>\n",
              "      <td>2</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>21</th>\n",
              "      <td>2021-01-22</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>45987</td>\n",
              "      <td>258</td>\n",
              "      <td>262</td>\n",
              "      <td>1.627329</td>\n",
              "      <td>upward</td>\n",
              "      <td>846</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>0.5</td>\n",
              "      <td>downward</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>2021-01-23</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>46239</td>\n",
              "      <td>252</td>\n",
              "      <td>232</td>\n",
              "      <td>1.669065</td>\n",
              "      <td>upward</td>\n",
              "      <td>848</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>0.5</td>\n",
              "      <td>downward</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23</th>\n",
              "      <td>2021-01-24</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>46429</td>\n",
              "      <td>190</td>\n",
              "      <td>238</td>\n",
              "      <td>1.535484</td>\n",
              "      <td>upward</td>\n",
              "      <td>850</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>0.5</td>\n",
              "      <td>downward</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>24</th>\n",
              "      <td>2021-01-25</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>Acre</td>\n",
              "      <td>881935</td>\n",
              "      <td>46539</td>\n",
              "      <td>110</td>\n",
              "      <td>252</td>\n",
              "      <td>1.431818</td>\n",
              "      <td>upward</td>\n",
              "      <td>854</td>\n",
              "      <td>4</td>\n",
              "      <td>3</td>\n",
              "      <td>1.0</td>\n",
              "      <td>stable</td>\n",
              "      <td>2021-01</td>\n",
              "      <td>2021</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "         date country state  population  confirmed  confirmed_1d  \\\n",
              "0  2021-01-01  Brazil  Acre      881935      41689          <NA>   \n",
              "1  2021-01-02  Brazil  Acre      881935      41941           252   \n",
              "2  2021-01-03  Brazil  Acre      881935      42046           105   \n",
              "3  2021-01-04  Brazil  Acre      881935      42117            71   \n",
              "4  2021-01-05  Brazil  Acre      881935      42170            53   \n",
              "5  2021-01-06  Brazil  Acre      881935      42378           208   \n",
              "6  2021-01-07  Brazil  Acre      881935      42478           100   \n",
              "7  2021-01-08  Brazil  Acre      881935      42814           336   \n",
              "8  2021-01-09  Brazil  Acre      881935      42908            94   \n",
              "9  2021-01-10  Brazil  Acre      881935      43127           219   \n",
              "10 2021-01-11  Brazil  Acre      881935      43346           219   \n",
              "11 2021-01-12  Brazil  Acre      881935      43432            86   \n",
              "12 2021-01-13  Brazil  Acre      881935      43785           353   \n",
              "13 2021-01-14  Brazil  Acre      881935      44068           283   \n",
              "14 2021-01-15  Brazil  Acre      881935      44156            88   \n",
              "15 2021-01-16  Brazil  Acre      881935      44621           465   \n",
              "16 2021-01-17  Brazil  Acre      881935      44767           146   \n",
              "17 2021-01-18  Brazil  Acre      881935      44775             8   \n",
              "18 2021-01-19  Brazil  Acre      881935      45208           433   \n",
              "19 2021-01-20  Brazil  Acre      881935      45429           221   \n",
              "20 2021-01-21  Brazil  Acre      881935      45729           300   \n",
              "21 2021-01-22  Brazil  Acre      881935      45987           258   \n",
              "22 2021-01-23  Brazil  Acre      881935      46239           252   \n",
              "23 2021-01-24  Brazil  Acre      881935      46429           190   \n",
              "24 2021-01-25  Brazil  Acre      881935      46539           110   \n",
              "\n",
              "    confirmed_moving_avg_7d  confirmed_moving_avg_7d_rate_14d confirmed_trend  \\\n",
              "0                      <NA>                               NaN             NaN   \n",
              "1                      <NA>                               NaN             NaN   \n",
              "2                      <NA>                               NaN             NaN   \n",
              "3                      <NA>                               NaN             NaN   \n",
              "4                      <NA>                               NaN             NaN   \n",
              "5                      <NA>                               NaN             NaN   \n",
              "6                      <NA>                               NaN             NaN   \n",
              "7                       161                               NaN             NaN   \n",
              "8                       139                               NaN             NaN   \n",
              "9                       155                               NaN             NaN   \n",
              "10                      176                               NaN             NaN   \n",
              "11                      181                               NaN             NaN   \n",
              "12                      201                               NaN             NaN   \n",
              "13                      228                               NaN             NaN   \n",
              "14                      192                               NaN             NaN   \n",
              "15                      245                               NaN             NaN   \n",
              "16                      235                               NaN             NaN   \n",
              "17                      205                               NaN             NaN   \n",
              "18                      254                               NaN             NaN   \n",
              "19                      235                               NaN             NaN   \n",
              "20                      238                               NaN             NaN   \n",
              "21                      262                          1.627329          upward   \n",
              "22                      232                          1.669065          upward   \n",
              "23                      238                          1.535484          upward   \n",
              "24                      252                          1.431818          upward   \n",
              "\n",
              "    deaths  deaths_1d  deaths_moving_avg_7d  deaths_moving_avg_7d_rate_14d  \\\n",
              "0      796       <NA>                  <NA>                            NaN   \n",
              "1      798          2                  <NA>                            NaN   \n",
              "2      802          4                  <NA>                            NaN   \n",
              "3      806          4                  <NA>                            NaN   \n",
              "4      808          2                  <NA>                            NaN   \n",
              "5      814          6                  <NA>                            NaN   \n",
              "6      821          7                  <NA>                            NaN   \n",
              "7      823          2                     4                            NaN   \n",
              "8      823          0                     4                            NaN   \n",
              "9      825          2                     4                            NaN   \n",
              "10     826          1                     3                            NaN   \n",
              "11     827          1                     3                            NaN   \n",
              "12     829          2                     3                            NaN   \n",
              "13     832          3                     2                            NaN   \n",
              "14     835          3                     2                            NaN   \n",
              "15     835          0                     2                            NaN   \n",
              "16     836          1                     2                            NaN   \n",
              "17     837          1                     2                            NaN   \n",
              "18     839          2                     2                            NaN   \n",
              "19     840          1                     2                            NaN   \n",
              "20     844          4                     2                            NaN   \n",
              "21     846          2                     2                            0.5   \n",
              "22     848          2                     2                            0.5   \n",
              "23     850          2                     2                            0.5   \n",
              "24     854          4                     3                            1.0   \n",
              "\n",
              "   deaths_trend    month  year  \n",
              "0           NaN  2021-01  2021  \n",
              "1           NaN  2021-01  2021  \n",
              "2           NaN  2021-01  2021  \n",
              "3           NaN  2021-01  2021  \n",
              "4           NaN  2021-01  2021  \n",
              "5           NaN  2021-01  2021  \n",
              "6           NaN  2021-01  2021  \n",
              "7           NaN  2021-01  2021  \n",
              "8           NaN  2021-01  2021  \n",
              "9           NaN  2021-01  2021  \n",
              "10          NaN  2021-01  2021  \n",
              "11          NaN  2021-01  2021  \n",
              "12          NaN  2021-01  2021  \n",
              "13          NaN  2021-01  2021  \n",
              "14          NaN  2021-01  2021  \n",
              "15          NaN  2021-01  2021  \n",
              "16          NaN  2021-01  2021  \n",
              "17          NaN  2021-01  2021  \n",
              "18          NaN  2021-01  2021  \n",
              "19          NaN  2021-01  2021  \n",
              "20          NaN  2021-01  2021  \n",
              "21     downward  2021-01  2021  \n",
              "22     downward  2021-01  2021  \n",
              "23     downward  2021-01  2021  \n",
              "24       stable  2021-01  2021  "
            ]
          },
          "execution_count": 17,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "cases.head(n=25)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KaLl8zdofQwE"
      },
      "source": [
        "#### **2.1.3. Carregamento**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "b1vD9VLafQwG"
      },
      "source": [
        "Com os dados manipulados, vamos persisti-lo em disco, fazer o seu download e carrega-lo no Google Data Studio."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "id": "mAazd-g0fQwG"
      },
      "outputs": [],
      "source": [
        "cases.to_csv('./covid-cases.csv', sep=',', index=False)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ndJlwEdGpvRO"
      },
      "source": [
        "### **2.2. Vacinação**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4KimqDnGbHbI"
      },
      "source": [
        "Vamos processar os dados de **vacinação** da universidade de Oxford."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3SsBfzTOUwZh"
      },
      "source": [
        "#### **2.2.1. Extração**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "k6ZYYdAKRQGS"
      },
      "source": [
        "Os dados estão compilados em um único arquivo."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G8nM5lc0USbd",
        "outputId": "5b50d250-bd0e-4fef-ff11-effefed80d57"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/tmp/ipykernel_34563/738699849.py:1: FutureWarning: The argument 'infer_datetime_format' is deprecated and will be removed in a future version. A strict version of it is now the default, see https://pandas.pydata.org/pdeps/0004-consistent-to-datetime-parsing.html. You can safely remove this argument.\n",
            "  vaccines = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', sep=',', parse_dates=[3], infer_datetime_format=True)\n"
          ]
        }
      ],
      "source": [
        "vaccines = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', sep=',', parse_dates=[3], infer_datetime_format=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 342
        },
        "id": "UCLtev1dUnuY",
        "outputId": "9799c1d3-b30e-4224-8c55-8f2364d4040d"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>iso_code</th>\n",
              "      <th>continent</th>\n",
              "      <th>location</th>\n",
              "      <th>date</th>\n",
              "      <th>total_cases</th>\n",
              "      <th>new_cases</th>\n",
              "      <th>new_cases_smoothed</th>\n",
              "      <th>total_deaths</th>\n",
              "      <th>new_deaths</th>\n",
              "      <th>new_deaths_smoothed</th>\n",
              "      <th>...</th>\n",
              "      <th>male_smokers</th>\n",
              "      <th>handwashing_facilities</th>\n",
              "      <th>hospital_beds_per_thousand</th>\n",
              "      <th>life_expectancy</th>\n",
              "      <th>human_development_index</th>\n",
              "      <th>population</th>\n",
              "      <th>excess_mortality_cumulative_absolute</th>\n",
              "      <th>excess_mortality_cumulative</th>\n",
              "      <th>excess_mortality</th>\n",
              "      <th>excess_mortality_cumulative_per_million</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>AFG</td>\n",
              "      <td>Asia</td>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>2020-01-05</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>37.746</td>\n",
              "      <td>0.5</td>\n",
              "      <td>64.83</td>\n",
              "      <td>0.511</td>\n",
              "      <td>41128772</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>AFG</td>\n",
              "      <td>Asia</td>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>2020-01-06</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>37.746</td>\n",
              "      <td>0.5</td>\n",
              "      <td>64.83</td>\n",
              "      <td>0.511</td>\n",
              "      <td>41128772</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>AFG</td>\n",
              "      <td>Asia</td>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>2020-01-07</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>37.746</td>\n",
              "      <td>0.5</td>\n",
              "      <td>64.83</td>\n",
              "      <td>0.511</td>\n",
              "      <td>41128772</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>AFG</td>\n",
              "      <td>Asia</td>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>2020-01-08</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>37.746</td>\n",
              "      <td>0.5</td>\n",
              "      <td>64.83</td>\n",
              "      <td>0.511</td>\n",
              "      <td>41128772</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>AFG</td>\n",
              "      <td>Asia</td>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>2020-01-09</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>37.746</td>\n",
              "      <td>0.5</td>\n",
              "      <td>64.83</td>\n",
              "      <td>0.511</td>\n",
              "      <td>41128772</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 67 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "  iso_code continent     location       date  total_cases  new_cases  \\\n",
              "0      AFG      Asia  Afghanistan 2020-01-05          0.0        0.0   \n",
              "1      AFG      Asia  Afghanistan 2020-01-06          0.0        0.0   \n",
              "2      AFG      Asia  Afghanistan 2020-01-07          0.0        0.0   \n",
              "3      AFG      Asia  Afghanistan 2020-01-08          0.0        0.0   \n",
              "4      AFG      Asia  Afghanistan 2020-01-09          0.0        0.0   \n",
              "\n",
              "   new_cases_smoothed  total_deaths  new_deaths  new_deaths_smoothed  ...  \\\n",
              "0                 NaN           0.0         0.0                  NaN  ...   \n",
              "1                 NaN           0.0         0.0                  NaN  ...   \n",
              "2                 NaN           0.0         0.0                  NaN  ...   \n",
              "3                 NaN           0.0         0.0                  NaN  ...   \n",
              "4                 NaN           0.0         0.0                  NaN  ...   \n",
              "\n",
              "   male_smokers  handwashing_facilities  hospital_beds_per_thousand  \\\n",
              "0           NaN                  37.746                         0.5   \n",
              "1           NaN                  37.746                         0.5   \n",
              "2           NaN                  37.746                         0.5   \n",
              "3           NaN                  37.746                         0.5   \n",
              "4           NaN                  37.746                         0.5   \n",
              "\n",
              "   life_expectancy  human_development_index  population  \\\n",
              "0            64.83                    0.511    41128772   \n",
              "1            64.83                    0.511    41128772   \n",
              "2            64.83                    0.511    41128772   \n",
              "3            64.83                    0.511    41128772   \n",
              "4            64.83                    0.511    41128772   \n",
              "\n",
              "   excess_mortality_cumulative_absolute  excess_mortality_cumulative  \\\n",
              "0                                   NaN                          NaN   \n",
              "1                                   NaN                          NaN   \n",
              "2                                   NaN                          NaN   \n",
              "3                                   NaN                          NaN   \n",
              "4                                   NaN                          NaN   \n",
              "\n",
              "   excess_mortality  excess_mortality_cumulative_per_million  \n",
              "0               NaN                                      NaN  \n",
              "1               NaN                                      NaN  \n",
              "2               NaN                                      NaN  \n",
              "3               NaN                                      NaN  \n",
              "4               NaN                                      NaN  \n",
              "\n",
              "[5 rows x 67 columns]"
            ]
          },
          "execution_count": 20,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "vaccines.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ImybLrrgRS4v"
      },
      "source": [
        "Vamos selecionar as colunas de interesse e as linhas referentes ao Brasil."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "id": "4RNfnnUZW6DY"
      },
      "outputs": [],
      "source": [
        "vaccines = vaccines.query('location == \"Brazil\"').reset_index(drop=True)\n",
        "vaccines = vaccines[['location', 'population', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'total_boosters', 'date']]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "e4kmFIpkPm1s",
        "outputId": "9cee9d18-9505-462b-90d7-6740b2520e61"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>location</th>\n",
              "      <th>population</th>\n",
              "      <th>total_vaccinations</th>\n",
              "      <th>people_vaccinated</th>\n",
              "      <th>people_fully_vaccinated</th>\n",
              "      <th>total_boosters</th>\n",
              "      <th>date</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1669</th>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2024-07-31</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1670</th>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2024-08-01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1671</th>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2024-08-02</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1672</th>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2024-08-03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1673</th>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2024-08-04</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     location  population  total_vaccinations  people_vaccinated  \\\n",
              "1669   Brazil   215313504                 NaN                NaN   \n",
              "1670   Brazil   215313504                 NaN                NaN   \n",
              "1671   Brazil   215313504                 NaN                NaN   \n",
              "1672   Brazil   215313504                 NaN                NaN   \n",
              "1673   Brazil   215313504                 NaN                NaN   \n",
              "\n",
              "      people_fully_vaccinated  total_boosters       date  \n",
              "1669                      NaN             NaN 2024-07-31  \n",
              "1670                      NaN             NaN 2024-08-01  \n",
              "1671                      NaN             NaN 2024-08-02  \n",
              "1672                      NaN             NaN 2024-08-03  \n",
              "1673                      NaN             NaN 2024-08-04  "
            ]
          },
          "execution_count": 26,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "vaccines.tail()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ANfJty-Iff4F"
      },
      "source": [
        "#### **2.2.2. Wrangling**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XVh6eEL3zSqm"
      },
      "source": [
        "Vamos manipular os dados para o dashboard. O foco é em garantir uma boa granularidade e qualidade da base de dados."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "zl5Elp43flYU",
        "outputId": "40b7d03f-a5e7-481f-868f-15de14b7a507"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>location</th>\n",
              "      <th>population</th>\n",
              "      <th>total_vaccinations</th>\n",
              "      <th>people_vaccinated</th>\n",
              "      <th>people_fully_vaccinated</th>\n",
              "      <th>total_boosters</th>\n",
              "      <th>date</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2020-01-05</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2020-01-06</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2020-01-07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2020-01-08</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>2020-01-09</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  location  population  total_vaccinations  people_vaccinated  \\\n",
              "0   Brazil   215313504                 NaN                NaN   \n",
              "1   Brazil   215313504                 NaN                NaN   \n",
              "2   Brazil   215313504                 NaN                NaN   \n",
              "3   Brazil   215313504                 NaN                NaN   \n",
              "4   Brazil   215313504                 NaN                NaN   \n",
              "\n",
              "   people_fully_vaccinated  total_boosters       date  \n",
              "0                      NaN             NaN 2020-01-05  \n",
              "1                      NaN             NaN 2020-01-06  \n",
              "2                      NaN             NaN 2020-01-07  \n",
              "3                      NaN             NaN 2020-01-08  \n",
              "4                      NaN             NaN 2020-01-09  "
            ]
          },
          "execution_count": 23,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "vaccines.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GOH412CJflYV",
        "outputId": "fffa5c37-2f77-4b35-a87f-0a4a8dbc35a1"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(1674, 7)"
            ]
          },
          "execution_count": 24,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "vaccines.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QV6H5gl6flYW",
        "outputId": "5838792f-227d-4bb6-eb27-262fd78fa40d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1674 entries, 0 to 1673\n",
            "Data columns (total 7 columns):\n",
            " #   Column                   Non-Null Count  Dtype         \n",
            "---  ------                   --------------  -----         \n",
            " 0   location                 1674 non-null   object        \n",
            " 1   population               1674 non-null   int64         \n",
            " 2   total_vaccinations       695 non-null    float64       \n",
            " 3   people_vaccinated        691 non-null    float64       \n",
            " 4   people_fully_vaccinated  675 non-null    float64       \n",
            " 5   total_boosters           455 non-null    float64       \n",
            " 6   date                     1674 non-null   datetime64[ns]\n",
            "dtypes: datetime64[ns](1), float64(4), int64(1), object(1)\n",
            "memory usage: 91.7+ KB\n"
          ]
        }
      ],
      "source": [
        "vaccines.info()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "L5CaqVEzzaYH"
      },
      "source": [
        "Vamos começar tratando os dados faltantes, a estratégia será a de preencher os buracos com o valor anterior válido mais próximo."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7UlhJa5M0fMz",
        "outputId": "e958f518-18e0-4eb6-a684-88ed1b27d778"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/tmp/ipykernel_34563/1781271583.py:1: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.\n",
            "  vaccines = vaccines.fillna(method='ffill')\n"
          ]
        }
      ],
      "source": [
        "vaccines = vaccines.fillna(method='ffill')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GibNnv1hfe8t"
      },
      "source": [
        "Vamos também filtrar a base de dados de acordo com a coluna `date` para garantir que ambas as bases de dados tratam do mesmo período de tempo."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "metadata": {
        "id": "bB8n5Nq0e51M"
      },
      "outputs": [],
      "source": [
        "vaccines = vaccines[(vaccines['date'] >= '2021-01-01') & (vaccines['date'] <= '2024-08-04')].reset_index(drop=True)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HeVzXS5pzUyh"
      },
      "source": [
        "Agora, vamos alterar o nome das colunas."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 29,
      "metadata": {
        "id": "onD0FAQ2fuZG"
      },
      "outputs": [],
      "source": [
        "vaccines = vaccines.rename(\n",
        "  columns={\n",
        "    'location': 'country',\n",
        "    'total_vaccinations': 'total',\n",
        "    'people_vaccinated': 'one_shot',\n",
        "    'people_fully_vaccinated': 'two_shots',\n",
        "    'total_boosters': 'three_shots',\n",
        "  }\n",
        ")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3WEwZVW8zZdQ"
      },
      "source": [
        "Vamos então computar novas colunas para enriquecer a base de dados."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TtVVYdEn1xBu"
      },
      "source": [
        " - Chaves temporais:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 30,
      "metadata": {
        "id": "69n_u8z-fuZI"
      },
      "outputs": [],
      "source": [
        "vaccines['month'] = vaccines['date'].apply(lambda date: date.strftime('%Y-%m'))\n",
        "vaccines['year']  = vaccines['date'].apply(lambda date: date.strftime('%Y'))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RToFxe8s13WZ"
      },
      "source": [
        " - Dados relativos:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 31,
      "metadata": {
        "id": "0p5fH8yI160u"
      },
      "outputs": [],
      "source": [
        "vaccines['one_shot_perc'] = round(vaccines['one_shot'] / vaccines['population'], 4)\n",
        "vaccines['two_shots_perc'] = round(vaccines['two_shots'] / vaccines['population'], 4)\n",
        "vaccines['three_shots_perc'] = round(vaccines['three_shots'] / vaccines['population'], 4)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AwBPeUoH018t"
      },
      "source": [
        "Garantir o tipo do dado é fundamental para consistência da base de dados. Vamos fazer o *type casting* das colunas."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 32,
      "metadata": {
        "id": "bkebNuXF024g"
      },
      "outputs": [],
      "source": [
        "vaccines['population'] = vaccines['population'].astype('Int64')\n",
        "vaccines['total'] = vaccines['total'].astype('Int64')\n",
        "vaccines['one_shot'] = vaccines['one_shot'].astype('Int64')\n",
        "vaccines['two_shots'] = vaccines['two_shots'].astype('Int64')\n",
        "vaccines['three_shots'] = vaccines['three_shots'].astype('Int64')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "R8s4jBC4gUrq"
      },
      "source": [
        "Por fim, vamos reorganizar as colunas e conferir o resultado final."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 33,
      "metadata": {
        "id": "GRqAQTFxfuZJ"
      },
      "outputs": [],
      "source": [
        "vaccines = vaccines[['date', 'country', 'population', 'total', 'one_shot', 'one_shot_perc', 'two_shots', 'two_shots_perc', 'three_shots', 'three_shots_perc', 'month', 'year']]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 34,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "RqeuGtCPzXmj",
        "outputId": "ea24e386-d2b2-46d3-c678-70c8cc92e5cf"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>date</th>\n",
              "      <th>country</th>\n",
              "      <th>population</th>\n",
              "      <th>total</th>\n",
              "      <th>one_shot</th>\n",
              "      <th>one_shot_perc</th>\n",
              "      <th>two_shots</th>\n",
              "      <th>two_shots_perc</th>\n",
              "      <th>three_shots</th>\n",
              "      <th>three_shots_perc</th>\n",
              "      <th>month</th>\n",
              "      <th>year</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1307</th>\n",
              "      <td>2024-07-31</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>486436436</td>\n",
              "      <td>189643431</td>\n",
              "      <td>0.8808</td>\n",
              "      <td>176164186</td>\n",
              "      <td>0.8182</td>\n",
              "      <td>126388587</td>\n",
              "      <td>0.587</td>\n",
              "      <td>2024-07</td>\n",
              "      <td>2024</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1308</th>\n",
              "      <td>2024-08-01</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>486436436</td>\n",
              "      <td>189643431</td>\n",
              "      <td>0.8808</td>\n",
              "      <td>176164186</td>\n",
              "      <td>0.8182</td>\n",
              "      <td>126388587</td>\n",
              "      <td>0.587</td>\n",
              "      <td>2024-08</td>\n",
              "      <td>2024</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1309</th>\n",
              "      <td>2024-08-02</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>486436436</td>\n",
              "      <td>189643431</td>\n",
              "      <td>0.8808</td>\n",
              "      <td>176164186</td>\n",
              "      <td>0.8182</td>\n",
              "      <td>126388587</td>\n",
              "      <td>0.587</td>\n",
              "      <td>2024-08</td>\n",
              "      <td>2024</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1310</th>\n",
              "      <td>2024-08-03</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>486436436</td>\n",
              "      <td>189643431</td>\n",
              "      <td>0.8808</td>\n",
              "      <td>176164186</td>\n",
              "      <td>0.8182</td>\n",
              "      <td>126388587</td>\n",
              "      <td>0.587</td>\n",
              "      <td>2024-08</td>\n",
              "      <td>2024</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1311</th>\n",
              "      <td>2024-08-04</td>\n",
              "      <td>Brazil</td>\n",
              "      <td>215313504</td>\n",
              "      <td>486436436</td>\n",
              "      <td>189643431</td>\n",
              "      <td>0.8808</td>\n",
              "      <td>176164186</td>\n",
              "      <td>0.8182</td>\n",
              "      <td>126388587</td>\n",
              "      <td>0.587</td>\n",
              "      <td>2024-08</td>\n",
              "      <td>2024</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "           date country  population      total   one_shot  one_shot_perc  \\\n",
              "1307 2024-07-31  Brazil   215313504  486436436  189643431         0.8808   \n",
              "1308 2024-08-01  Brazil   215313504  486436436  189643431         0.8808   \n",
              "1309 2024-08-02  Brazil   215313504  486436436  189643431         0.8808   \n",
              "1310 2024-08-03  Brazil   215313504  486436436  189643431         0.8808   \n",
              "1311 2024-08-04  Brazil   215313504  486436436  189643431         0.8808   \n",
              "\n",
              "      two_shots  two_shots_perc  three_shots  three_shots_perc    month  year  \n",
              "1307  176164186          0.8182    126388587             0.587  2024-07  2024  \n",
              "1308  176164186          0.8182    126388587             0.587  2024-08  2024  \n",
              "1309  176164186          0.8182    126388587             0.587  2024-08  2024  \n",
              "1310  176164186          0.8182    126388587             0.587  2024-08  2024  \n",
              "1311  176164186          0.8182    126388587             0.587  2024-08  2024  "
            ]
          },
          "execution_count": 34,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "vaccines.tail()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yhTcLXpaV5-F"
      },
      "source": [
        "#### **2.2.3. Carregamento**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ciQaKaE8WDYL"
      },
      "source": [
        "Com os dados manipulados, vamos persisti-lo em disco, fazer o seu download e carrega-lo no Google Data Studio."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 35,
      "metadata": {
        "id": "ur-OHsXIWN_-"
      },
      "outputs": [],
      "source": [
        "vaccines.to_csv('./covid-vaccines.csv', sep=',', index=False)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PD0FiM7UJOGT"
      },
      "source": [
        "## 3\\. Exploração Interativa de Dados"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AAwJC4RyS0xa"
      },
      "source": [
        "### **3.1. KPIs**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9LIHnwDuiN47"
      },
      "source": [
        "O dashboard de dados contem os seguintes indicadores chaves de desempenho (*key performance indicator* ou KPI) consolidados:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rllIx255dOOu"
      },
      "source": [
        "1. Casos e mortes nas 24 horas;\n",
        "1. Média móvel (7 dias) de casos e mortes;\n",
        "1. Tendência de casos e mortes;\n",
        "1. Proporção de vacinados com 1ª, 2ª e 3ª doses."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QGWv8lw5YdUC"
      },
      "source": [
        "### **3.2. EDA**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AZPbGM3cdOyi"
      },
      "source": [
        "O dashboard de dados contem os seguintes gráficos para a análise exploratória de dados (*exploratory data analysis*\n",
        "ou EDA) interativa:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QuzfB5PmYjS9"
      },
      "source": [
        "1. Distribuição do números de casos e mortes ao longo do tempo;\n",
        "1. Distribuição da média móvel (7 dias) do números de casos e mortes ao longo do tempo;\n",
        "1. Distribuição geográfica dos casos por estado por dia."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fGmO0I_ae62k"
      },
      "source": [
        "## 4\\. Storytelling"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Dados sobre Casos e Vacinação da COVID-19\n",
        "\n",
        "## Contexto\n",
        "A pandemia de COVID-19 trouxe desafios globais sem precedentes, destacando a importância de dados confiáveis para informar a tomada de decisão. Através da análise dos dados compilados pela Universidade John Hopkins, buscamos entender a dinâmica de casos, mortes e vacinações ao longo do tempo e em diferentes regiões geográficas.\n",
        "\n",
        "## Objetivo\n",
        "O objetivo principal desta análise é fornecer insights significativos sobre a evolução da pandemia e os avanços na vacinação, de forma a apoiar decisões baseadas em dados.\n",
        "\n",
        "---\n",
        "\n",
        "## Principais Insights\n",
        "\n",
        "### 1. **Casos e Mortes nas últimas 24 horas**\n",
        "- **Casos registrados:** A variação diária fornece um panorama imediato da disseminação do vírus.\n",
        "- **Mortes registradas:** Este KPI destaca os impactos mais graves da pandemia e auxilia na avaliação de regiões mais afetadas.\n",
        "\n",
        "### 2. **Média Móvel (7 dias)**\n",
        "- A média móvel de casos e mortes ajuda a suavizar flutuações diárias e a identificar tendências consistentes.\n",
        "\n",
        "### 3. **Tendência de Casos e Mortes**\n",
        "- Análise de longo prazo revelou picos durante ondas de novas variantes e reduções após campanhas de vacinação bem-sucedidas.\n",
        "\n",
        "### 4. **Distribuição Geográfica dos Casos**\n",
        "- Identificamos regiões mais afetadas, destacando a necessidade de alocação direcionada de recursos.\n",
        "\n",
        "### 5. **Vacinação**\n",
        "- Proporção de vacinados com:\n",
        "  - **1ª dose:** Indicativo do alcance inicial das campanhas.\n",
        "  - **2ª dose:** Métrica de imunização completa.\n",
        "  - **3ª dose:** Reflete a adesão às doses de reforço.\n",
        "\n",
        "---\n",
        "\n",
        "## Histórias dos Dados\n",
        "\n",
        "### **A Expansão Global do Vírus**\n",
        "- No início da pandemia, os casos se concentravam em poucas regiões, mas rapidamente se disseminaram. Análises temporais mostraram o impacto de medidas como lockdowns e uso de máscaras.\n",
        "\n",
        "### **Ondas de Infecção**\n",
        "- Ondas sucessivas de infecções coincidiram com o surgimento de novas variantes, sendo marcadas por aumentos abruptos nos indicadores de casos e mortes.\n",
        "\n",
        "### **Impacto das Vacinas**\n",
        "- Após o lançamento das vacinas, observou-se uma redução consistente na taxa de mortalidade e na gravidade dos casos em populações amplamente vacinadas.\n",
        "\n",
        "### **Desigualdade Regional**\n",
        "- Análises geográficas revelaram desigualdades no acesso à vacinação e no impacto da pandemia. Regiões menos desenvolvidas apresentaram taxas de mortalidade mais altas.\n",
        "\n",
        "---\n",
        "\n",
        "## Visualizações Relevantes\n",
        "\n",
        "1. **Linha do Tempo da Pandemia**\n",
        "   - Evolução dos casos e mortes.\n",
        "\n",
        "2. **Mapas Geográficos**\n",
        "   - Distribuição de casos e vacinas por região.\n",
        "\n",
        "3. **Gráficos de Médias Móveis**\n",
        "   - Comparativos de tendências entre períodos distintos.\n",
        "\n",
        "---\n",
        "\n",
        "## Conclusão\n",
        "A análise demonstrou como a combinação de medidas preventivas e vacinação em larga escala foi determinante para mitigar os impactos da pandemia. Destacou ainda a importância de monitorar indicadores de saúde para gestão eficaz de crises futuras.\n",
        "\n",
        "\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "base",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.12.4"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
