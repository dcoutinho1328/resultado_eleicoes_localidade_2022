def createLayout(sg):
    # Screens

    loadingScreen = [
        [
            sg.T(
                "Carregando Dados...",
                font=(20),
                justification="center",
                key="LOADING_TEXT",
            ),
            sg.Image(source="static/loading.gif", key="LOADGIF"),
        ]
    ]

    locationSelector = [
        [
            sg.T("UF", font=(20), justification="center", size=(3, None)),
            sg.DD(
                values=[],
                size=(8, None),
                key="UF",
                disabled=True,
                enable_events=True,
                readonly=True,
            ),
            sg.T(
                "Município", font=(20), justification="center", size=(10, None), key="M"
            ),
            sg.DD(
                values=[],
                size=(15, None),
                key="MUN",
                disabled=True,
                enable_events=True,
                readonly=True,
            ),
            sg.T(
                "Localidade",
                font=(20),
                justification="center",
                size=(10, None),
                key="L",
            ),
            sg.DD(
                values=[],
                size=(15, None),
                key="LOC",
                disabled=True,
                enable_events=True,
                readonly=True,
            ),
        ],
        [
            sg.Column(
                [[sg.B("Pesquisar", key="SEARCH", size=(20, None), disabled=True)]],
                justification="center",
            )
        ],
    ]

    resultScreen = [
        [
            sg.T(
                "",
                font=(20),
                justification="center",
                size=(30, None),
                key="DESCRIPTION",
                expand_x=True,
            )
        ],
        [
            sg.Column(
                [
                    [
                        sg.T("Lula", font=(30), key="LULA"),
                        sg.T("", font=(40), key="L-PERCENT"),
                    ],
                ]
            ),
            sg.Column(
                [
                    [
                        sg.T("Bolsonaro", font=(30), key="BOLSONARO"),
                        sg.T("", font=(40), key="B-PERCENT"),
                    ],
                ]
            ),
        ],
        [
            sg.Column(
                [[sg.B("Voltar", key="BACK", size=(20, None))]], justification="center"
            )
        ],
    ]

    # Main Layout

    layout = [
        [
            sg.pin(
                sg.Column(
                    loadingScreen, key="LOADING", justification="center", visible=False
                )
            )
        ],
        [
            sg.pin(
                sg.Column(
                    locationSelector,
                    key="LOCATION",
                    justification="center",
                    visible=False,
                )
            )
        ],
        [
            sg.pin(
                sg.Column(
                    resultScreen, key="RESULT", justification="center", visible=False
                )
            )
        ],
    ]

    return layout
