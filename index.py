from uiBuilder.eventHandler import handleEvents
from uiBuilder import createWindow

app_name = "Votos por Localidade - Eleições 2022"
app_icon = "./static/icon.ico"

if __name__ == "__main__":
    # Removes splash image on deploy
    try:
        import pyi_splash

        pyi_splash.close()
    except:
        pass
    window = createWindow(app_name, app_icon)
    handleEvents(window)
