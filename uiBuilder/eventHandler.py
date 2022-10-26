import threading
from dataHandler import loadData
from dataHandler.dataBase import getLocations, getValues
import PySimpleGUI as sg
from os.path import exists
import json


def handleEvents(window):

    # Define Components

    loading = window["LOADING"]
    uf = window["UF"]
    mun = window["MUN"]
    loc = window["LOC"]
    mun_t = window["M"]
    loc_t = window["L"]
    locSel = window["LOCATION"]
    search = window["SEARCH"]
    result = window["RESULT"]
    lula = window["LULA"]
    bolsonaro = window["BOLSONARO"]
    lulaPercent = window["L-PERCENT"]
    bolsonaroPercent = window["B-PERCENT"]
    description = window["DESCRIPTION"]

    # Init flags and globals

    loadingStatus = False
    loaded = False
    locations = None
    dataBase = None
    redBG = "#C15226"
    blueBG = "#3B49A8"
    defaultBG = "#282923"

    # Define util functions

    def populate():
        if not exists("./static/data.json"):
            window.write_event_value("LOAD_FROM_XLSX", "")
            data = loadData()
            locations = getLocations(data)
            dataBase = getValues(data)
            data = {"locations": locations, "dataBase": dataBase}
            with open("./static/data.json", "w") as file:
                file.write(json.dumps(data))
        else:
            window.write_event_value("LOAD_FROM_JSON", "")
            file = open("./static/data.json", "r")
            data = json.loads(file.read())
            file.close()
        window.write_event_value("DATA_LOADED", data)

    def findValue(u, m, l):
        if u == "Exterior":
            u = "ZZ"
            aux = l
            l = m
            m = aux
        found = list(
            filter(
                lambda x: x["UF"] == u
                and x["MUNICIPIO"] == m
                and x["BAIRRO/LOCALIDADE"] == l,
                dataBase,
            )
        )
        window.write_event_value("FOUND", found[0] if len(found) > 0 else None)

    # Start looping

    while True:
        event, values = window.read(timeout=10)

        if event == sg.WIN_CLOSED:
            break

        if not loaded and not loadingStatus:
            loadingStatus = True
            loading.update(visible=True)
            thread = threading.Thread(target=populate, args=())
            thread.start()

        if loadingStatus:
            window.Element("LOADGIF").UpdateAnimation(
                "static/loading.gif", time_between_frames=20
            )

        if event == "LOAD_FROM_XLSX":
            window["LOADING_TEXT"].update("Carregando dados do XLSX...")

        if event == "LOAD_FROM_JSON":
            window["LOADING_TEXT"].update("Carregando dados do JSON...")

        if event == "DATA_LOADED":
            data = values[event]
            locations = data["locations"]
            dataBase = data["dataBase"]
            loadingStatus = False
            loaded = True
            loading.update(visible=False)
            locSel.update(visible=True)
            uf.update(disabled=False, values=list(locations.keys()))

        if event == "UF":
            u = values[event]
            if u == "Exterior":
                mun_t.update("País")
                loc_t.update("Cidade")
            else:
                mun_t.update("Município")
                loc_t.update("Localidade")
            mun.update(disabled=False, values=list(locations[u].keys()))
            loc.update(disabled=True, values=[])

        if event == "MUN":
            m = values[event]
            u = values["UF"]
            loc.update(disabled=False, values=list(locations[u][m]))

        if event == "LOC":
            search.update(disabled=False)

        if event == "SEARCH":
            thread = threading.Thread(
                target=findValue, args=(values["UF"], values["MUN"], values["LOC"])
            )
            thread.start()

        if event == "FOUND":
            found = values[event]
            locSel.update(visible=False)
            if found:
                lulaPercent.update(f"{found['Lula']*100:.2f} %")
                bolsonaroPercent.update(f"{found['Bolsonaro']*100:.2f} %")
                if found["Lula"] > found["Bolsonaro"]:
                    lula.update(background_color=redBG)
                elif found["Lula"] == found["Bolsonaro"]:
                    lula.update(background_color=redBG)
                    bolsonaro.update(background_color=blueBG)
                else:
                    bolsonaro.update(background_color=blueBG)
                if found["UF"] == "Exterior":
                    description.update(
                        f"{found['MUNICIPIO']}, {found['BAIRRO/LOCALIDADE']} - {found['UF']}"
                    )
                else:
                    description.update(
                        f"{found['BAIRRO/LOCALIDADE']}, {found['MUNICIPIO']} - {found['UF']}"
                    )
                result.update(visible=True)

        if event == "BACK":
            result.update(visible=False)
            mun_t.update("Município")
            loc_t.update("Localidade")
            lula.update(background_color=defaultBG)
            bolsonaro.update(background_color=defaultBG)
            uf.update(disabled=False, values=list(locations.keys()))
            mun.update(disabled=True, values=[])
            loc.update(disabled=True, values=[])
            locSel.update(visible=True)

    window.close()
