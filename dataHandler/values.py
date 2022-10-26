def getValues(data):
    keys = []
    base = []

    for key in data:
        keys.append(key)

    for item in data.values:
        base.append(dict(zip(keys, item)))

    return base
