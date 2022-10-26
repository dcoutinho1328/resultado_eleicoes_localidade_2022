def getLocations(data):
    def __filterMunByUf(uf):
        if uf == "ZZ":
            return sorted(set(data[data["UF"] == uf]["BAIRRO/LOCALIDADE"].tolist()))
        return sorted(set(data[data["UF"] == uf]["MUNICIPIO"].tolist()))

    def __filterLocByMunUF(mun, uf):
        dl2 = data[data["UF"] == uf]
        if uf == "ZZ":
            locs = list(
                map(
                    lambda x: str(x),
                    dl2[dl2["BAIRRO/LOCALIDADE"] == mun]["MUNICIPIO"].tolist(),
                )
            )
            locs.sort()
            return locs
        locs = list(
            map(
                lambda x: str(x),
                dl2[dl2["MUNICIPIO"] == mun]["BAIRRO/LOCALIDADE"].tolist(),
            )
        )
        locs.sort()
        return locs

    __dataDict = {}

    __ufList = sorted(set(data["UF"].tolist()))

    for uf in __ufList:
        __dataDict[uf] = {}
        for mun in __filterMunByUf(uf):
            __dataDict[uf][mun] = []
            for loc in __filterLocByMunUF(mun, uf):
                __dataDict[uf][mun].append(loc)

    __dataDict["Exterior"] = __dataDict["ZZ"]
    del __dataDict["ZZ"]

    return __dataDict


def getValues(data):
    keys = []
    base = []

    for key in data:
        keys.append(key)

    for item in data.values:
        base.append(dict(zip(keys, item)))

    return base
