from .layout import createLayout


def createWindow(name="", icon=""):
    import PySimpleGUI as sg

    sg.theme("Topanga")
    window = sg.Window(
        name,
        createLayout(sg),
        icon=icon,
        element_justification="center",
    )
    return window
