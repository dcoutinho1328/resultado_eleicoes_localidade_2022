pyinstaller index.py -w -n "Votos por Localidade - Eleicoes 2022" ^
    -i "./static/icon.ico" ^
    --splash "./static/icon.ico" ^
    --add-data="./static/icon.ico;static" ^
    --add-data="./static/data.xlsx;static" ^
    --add-data="./static/loading.gif;static"