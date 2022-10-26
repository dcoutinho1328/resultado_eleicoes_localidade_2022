from pandas import read_excel


def loadData():
    data = read_excel(
        "./static/data.xlsx",
        usecols=["UF", "MUNICIPIO", "BAIRRO/LOCALIDADE", "Lula", "Bolsonaro"],
    )
    return data
